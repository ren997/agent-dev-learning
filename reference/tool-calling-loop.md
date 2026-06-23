# Agent 工具调用循环速查

## 先记一句话

**模型提请求，代码干实事，结果再回模型。**

## 四个最关键的词

### `tools`

你提供给模型的工具清单。
它像一份菜单，告诉模型“你能用哪些外部能力”。

### `tool_call`

模型发出的工具调用请求。
它只是在说：

```text
我想调用某个工具，请帮我执行
```

它不是工具结果。

### `tool_result`

应用代码真正执行工具后的返回结果。

### `messages`

不只是聊天记录。
它也是 Agent 当前任务的状态记录。

## 最小流程

```text
1. 用户提出任务
2. 程序把 messages 和 tools 发给模型
3. 模型返回：
   - 直接回答
   - 或 tool_call 请求
4. 程序解析 tool_call
5. 程序执行对应 Python 函数
6. 程序把 tool_result 追加回 messages
7. 程序再次请求模型
8. 模型决定继续调用工具，或给出最终回答
```

## 一眼看懂边界

- 模型负责“决定下一步”
- 工具负责“真正做事”
- 应用代码负责“把两边接起来”

## 一个最小例子

用户说：

```text
计算 23 * 19，然后解释结果
```

模型可能返回：

```json
{"name": "calculator", "arguments": {"expression": "23 * 19"}}
```

这时应用代码执行：

```python
calculator("23 * 19")
```

拿到结果：

```text
437
```

再把这个结果放回 `messages`，模型才能继续回答：

```text
23 * 19 = 437。这个结果表示...
```

## 为什么需要循环

因为模型可能：

- 不需要工具
- 调用一个工具
- 调用多个工具

所以程序通常写成：

```python
while True:
    ask_model()
    if need_tool:
        run_tool()
        send_result_back()
        continue
    break
```

## 自查 3 问

1. `tool_call` 和 `tool_result` 的区别是什么？
2. 为什么工具执行结果不能只 print，而要回到 `messages`？
3. 为什么这个过程通常要用 `while` 循环？
