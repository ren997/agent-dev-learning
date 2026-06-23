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
    "system_prompt": "你是一个耐心的 Agent 开发学习助手，用简洁中文回答。",
}


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


def main() -> None:
    configure_console_encoding()
    config = load_config()
    client = build_client(config)
    model = os.getenv("OPENAI_MODEL", config["model"])

    user_input = input("请输入你的问题：").strip()
    if not user_input:
        print("问题不能为空。")
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

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )
    except APIConnectionError:
        print("连接模型服务失败。请检查网络、base_url，或稍后重试。")
        return

    answer = response.choices[0].message.content
    print("\n模型回答：")
    print(answer)


if __name__ == "__main__":
    main()
