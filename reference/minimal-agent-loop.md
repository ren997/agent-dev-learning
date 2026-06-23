# 最小 Agent Loop 速查

## 一句话

**Agent 不是模型自己去做事，而是模型提出行动请求，应用代码执行，再把结果反馈回模型。**

## 三个角色

- `Model`：判断要不要调用工具，调用哪个工具，参数是什么
- `Tool`：普通 Python 函数，真正执行外部能力
- `App Code`：维护循环、校验参数、执行工具、回传结果

## 最小流程

```text
1. 用户输入目标
2. 把 messages 和 tools 发给模型
3. 模型返回：
   - 要么是最终回答
   - 要么是 tool call request
4. Python 执行工具
5. 把 tool result 追加回 messages
6. 再次调用模型
7. 直到模型给出最终回答
```

## 最小伪代码

```python
while True:
    response = call_model(messages, tools)
    message = response.choices[0].message

    if message.tool_calls:
        messages.append(message)
        result = run_tool(...)
        messages.append(tool_result)
        continue

    print(message.content)
    break
```

## 关键边界

- 模型不会直接执行 Python 函数
- 模型只会返回“我想调用某个工具”的请求
- 真正执行工具的是你的应用代码
- 工具结果不回给模型，模型就无法继续判断下一步

## 什么时候更像 Chatbot

- 只做 `user -> model -> answer`
- 没有工具
- 没有循环
- 没有根据中间结果继续决策

## 什么时候开始像 Agent

- 模型能在运行时决定是否调用工具
- 工具执行结果会反馈回模型
- 模型能继续决定下一步

## 读代码时先盯这几个名字

- `tools`
- `tool_calls`
- `tool_call_id`
- `messages`
- `while True`

## 调试检查表

- `tools=[...]` 有没有传给模型
- `message.tool_calls` 有没有被正确判断
- 工具名有没有和 Python 函数映射上
- `arguments` 有没有被解析成字典
- 工具结果有没有追加回 `messages`
- 追加工具结果后有没有再次请求模型
