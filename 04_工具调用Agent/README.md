# 04 工具调用 Agent

本阶段目标：把前一阶段的最小 Chatbot 升级成一个会调用工具的最小 Agent。

对应课程：

- `../lessons/0004-build-first-tool-agent.md`

## 目录说明

- `mini_agent.py`：最小工具调用 Agent 代码
- `config.example.json`：配置样例

## 准备环境

安装依赖：

```bash
pip install openai
```

准备配置文件：

```bash
copy config.example.json config.json
```

如果你已经在 `02_大模型API调用/` 里配好了 `config.json`，也可以直接复制过来：

```bash
copy ..\02_大模型API调用\config.json .\config.json
```

学习阶段可以把 `api_key` 写进 `config.json`。这个文件已被 `.gitignore` 忽略，不要提交到 Git。

## 运行

```bash
python mini_agent.py
```

## 本阶段完成标准

- 能运行 `mini_agent.py`
- 能解释 `tool_call` 和 `tool_result` 的区别
- 能说清模型、工具和应用代码分别负责什么
- 能看懂工具结果为什么要追加回 `messages`
