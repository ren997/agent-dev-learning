# Agent 开发 Resources

## Knowledge

- [OpenAI API: Function calling](https://developers.openai.com/api/docs/guides/function-calling)
  官方函数调用文档。用于学习如何把 Python 函数暴露给模型，让模型输出结构化参数，由应用代码执行。

- [OpenAI API: Using tools](https://developers.openai.com/api/docs/guides/tools)
  官方工具总览。用于理解 function calling、内置工具、远程 MCP 工具等能力如何组成 Agent 的工具层。

- [OpenAI Cookbook: How to call functions with chat models](https://developers.openai.com/cookbook/examples/how_to_call_functions_with_chat_models/)
  官方示例教程。用于阶段三手写工具调用循环时参考请求、解析工具调用、执行函数、回传结果的完整流程。

- [Anthropic Docs: Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
  官方工具调用概念文档。用于从另一个主流模型供应商视角理解 agentic loop、client tools、server tools 和 tool_result。

- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
  LangGraph 官方总览。用于后期学习状态化、可持久化、可调试的 Agent 编排。

- [LangGraph Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api)
  LangGraph 官方 Graph API 文档。用于理解 State、Node、Edge 如何构建可循环和可分支的 Agent 工作流。

- [OpenAI Agents SDK: Tracing module](https://openai.github.io/openai-agents-python/ref/tracing/)
  OpenAI Agents SDK 追踪文档。用于后期学习如何观察 Agent 执行过程、工具调用和 handoff。

## Wisdom (Communities)

- [LangChain Forum](https://forum.langchain.com/)
  Agent 框架实践社区。用于遇到 LangGraph、LangChain 生态问题时查找真实项目中的经验。

- [OpenAI Developer Community](https://community.openai.com/)
  OpenAI 开发者社区。用于查询 API、工具调用、模型行为和生产实践相关讨论。

## Gaps

- 还需要补充一个适合中文学习者的 Agent 入门系列。
- 后续进入 RAG 阶段时，需要补充向量数据库、Embedding 和文档切分的官方资源。
- 后续进入部署阶段时，需要补充 FastAPI、Streamlit 或 LangGraph 部署相关资源。
