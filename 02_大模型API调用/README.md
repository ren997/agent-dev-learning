# 02 大模型 API 调用

本阶段目标：用 Python 调通大模型 API，做出一个最小命令行聊天程序。

对应课程：

- `../lessons/0002-call-llm-api.md`

## 准备环境

安装依赖：

```bash
pip install openai
```

复制配置文件：

```bash
copy config.example.json config.json
```

然后按你的模型供应商修改 `config.json`。

DeepSeek 示例：

```json
{
  "api_key": "你的 DeepSeek API Key",
  "base_url": "https://api.deepseek.com",
  "model": "deepseek-chat",
  "system_prompt": "你是一个耐心的 Agent 开发学习助手，用简洁中文回答。"
}
```

学习阶段可以把 `api_key` 写进 `config.json`。这个文件已被 `.gitignore` 忽略，不要提交到 Git。

## 运行

```bash
python simple_chat.py
```

## 本阶段完成标准

- 能解释 `API Key`、`client`、`model`、`messages`、`response`
- 能运行 `simple_chat.py`
- 能修改 `system` 提示词并观察输出变化
- 知道这个程序为什么还不是 Agent
