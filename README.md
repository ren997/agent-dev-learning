# Agent Dev Learning

这是一个个人 Agent 开发学习工作区，用来记录从基础概念到 Python 实战的学习过程。

## 学习目标

- 理解 Chatbot、Workflow、Agent 的区别
- 用 Python 调用大模型 API
- 手写最小 Agent 循环
- 学习工具调用、记忆、RAG 和 Agent 框架
- 最终完成一个个人学习助手 Agent

## 目录

- `agent学习计划.md`：整体学习路线
- `lessons/`：每节课内容
- `reference/`：术语表和速查资料
- `learning-records/`：关键学习记录
- `02_大模型API调用/`：第 0002 课代码练习，专门放最小 Chatbot
- `04_工具调用Agent/`：第 0004 课代码练习，专门放最小工具调用 Agent
- `MISSION.md`：学习任务目标
- `RESOURCES.md`：学习资源清单
- `NOTES.md`：教学偏好和过程记录

## 目录约定

- `lessons/` 只放课程讲义，按 `0001`、`0002`、`0003` 这样的课程序号递增。
- `reference/` 只放跨课程复用的术语表、速查表和流程说明。
- 顶层带编号的实践目录只放代码和运行说明，编号默认对齐“实操课”而不是所有概念课。
- 纯概念课可以只有 `lessons/` 和 `reference/` 内容，不一定单独建顶层代码目录。
- 每个实践目录尽量自包含，至少有 `README.md`、代码文件，以及需要时提供 `config.example.json`。

当前约定：

- 第 `0002` 课对应 `02_大模型API调用/`
- 第 `0003` 课是概念课，没有单独代码目录
- 第 `0004` 课对应 `04_工具调用Agent/`

## 当前进度

- 已完成 Agent 基础概念
- 已完成用 Python 调用大模型 API 的最小 Chatbot
- 正在学习 Agent 工具调用循环

## 安装 Teach Skill

```bash
npx skills@latest add mattpocock/skills
```

安装后可使用 `/teach 继续教我 Agent 开发` 继续学习。

## 安全提醒

`02_大模型API调用/config.json` 和 `04_工具调用Agent/config.json` 用于本地保存 API Key，已被 `.gitignore` 忽略，不要提交到 Git。
