import json
import os
import sys
from pathlib import Path

from openai import APIConnectionError, OpenAI


CONFIG_PATH = Path(__file__).with_name("config.json")

DEFAULT_CONFIG = {
    "api_key": None,
    "base_url": None,
    "model": "gpt-4.1-mini",
    "system_prompt": "你是一个耐心的 Agent 开发学习助手。需要计算时优先调用 calculator 工具，用简洁中文回答。",
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "计算简单算术表达式，只支持数字、空格、括号和 + - * /",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "待计算的算术表达式，例如 23 * (19 + 1)",
                    }
                },
                "required": ["expression"],
            },
        },
    }
]


def configure_console_encoding() -> None:
    for stream_name in ("stdin", "stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return DEFAULT_CONFIG

    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        user_config = json.load(file)

    return DEFAULT_CONFIG | user_config


def build_client(config: dict) -> OpenAI:
    api_key = config.get("api_key") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("请先在 config.json 中设置 api_key，或设置环境变量 OPENAI_API_KEY。")
        sys.exit(1)

    base_url = config.get("base_url") or os.getenv("OPENAI_BASE_URL")
    if base_url:
        return OpenAI(api_key=api_key, base_url=base_url)

    return OpenAI(api_key=api_key)


def calculator(expression: str) -> str:
    # 这里只做学习演示，避免把任意用户输入直接交给 eval。
    allowed_chars = set("0123456789+-*/(). ")
    if any(char not in allowed_chars for char in expression):
        return "计算失败：只允许数字、空格、括号和 + - * /"

    try:
        result = eval(expression, {"__builtins__": {}}, {})
    except Exception as exc:
        return f"计算失败：{exc}"

    return str(result)


def main() -> None:
    configure_console_encoding()
    config = load_config()
    client = build_client(config)
    model = os.getenv("OPENAI_MODEL", config["model"])

    user_input = input("请输入你的任务：").strip()
    if not user_input:
        print("任务不能为空。")
        return

    messages = [
        {
            "role": "system",
            "content": config["system_prompt"],
        },
        {
            "role": "user",
            "content": user_input,
        },
    ]

    while True:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=TOOLS,
            )
        except APIConnectionError:
            print("连接模型服务失败。请检查网络、base_url，或稍后重试。")
            return
        message = response.choices[0].message

        if message.tool_calls:
            messages.append(message.model_dump(exclude_none=True))

            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name

                try:
                    arguments = json.loads(tool_call.function.arguments)
                except json.JSONDecodeError:
                    tool_result = "工具参数解析失败。"
                else:
                    if tool_name == "calculator":
                        tool_result = calculator(arguments.get("expression", ""))
                    else:
                        tool_result = f"未知工具：{tool_name}"

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result,
                    }
                )

            continue

        answer = message.content or ""
        print("\n最终回答：")
        print(answer)
        break


if __name__ == "__main__":
    main()
