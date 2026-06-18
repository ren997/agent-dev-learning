# Lesson 0002: 用 Python 调用大模型 API

这一课的目标是做出一个最小 Chatbot：用户输入一句话，程序把消息发给大模型 API，然后打印模型回答。

先不做 Agent。因为 Agent 的工具调用、记忆、规划，都是建立在“能稳定调用模型”的基础上。

## 本节你要掌握什么

- `API Key` 是访问模型服务的凭证。学习阶段可以放在本地 `config.json`，但不要提交到 Git。
- `client` 是 SDK 客户端，用来发送请求。
- `model` 决定你调用哪个模型。
- `config.json` 可以保存模型名、接口地址、system 提示词等非敏感配置。
- `messages` 是对话上下文，通常由 `system`、`user`、`assistant` 消息组成。
- `response` 是模型返回结果，程序需要从里面取出文本。

## 最小调用流程

```text
读取 API Key
创建 client
准备 messages
调用模型
读取 response
打印回答
```

## 三种消息角色

### system

定义模型的身份、规则和边界。

```json
{"role": "system", "content": "你是一个耐心的 Python 学习助手。"}
```

### user

用户输入的问题或任务。

```json
{"role": "user", "content": "解释一下 Python 的 list。"}
```

### assistant

模型历史回答。做连续对话时，要把之前的 assistant 回复也放进 `messages`。

```json
{"role": "assistant", "content": "Python 的 list 是一种有序可变容器。"}
```

## 为什么先学 Chatbot

Agent 比 Chatbot 多了“决策 + 工具 + 反馈循环”。

但如果你还不能稳定完成：

```text
用户输入 -> 模型回答
```

就很难继续做：

```text
用户目标 -> 模型判断是否调用工具 -> 执行工具 -> 回传结果 -> 模型继续决策
```

所以第二节先把最小模型调用打通。

## 今日练习

打开 `02_大模型API调用/simple_chat.py`，完成这几件事：

1. 安装依赖：`pip install openai`
2. 复制配置文件：`copy config.example.json config.json`
3. 修改 `config.json` 里的 `api_key`、`base_url`、`model` 和 `system_prompt`
4. 运行程序：`python simple_chat.py`
5. 输入一个问题，观察模型回答
6. 修改 `system_prompt`，观察回答风格变化

## 你应该能回答的问题

学完这一节，你应该能回答：

- 为什么不能把 API Key 写进代码？
不安全
- `system` 和 `user` 消息有什么区别？
一个是定义模型身份的 一个是用户的输入
- 为什么连续对话需要保存历史消息？
需要让模型有记忆功能 知道之前讲了什么
- 当前程序为什么还不是 Agent？
只是单纯的对话工具 没有决策 不能决定调用什么工具

## 下次继续

下次我们会把单轮聊天改成连续对话，让程序记住本轮会话里的上下文。
