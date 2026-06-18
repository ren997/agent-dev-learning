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
- `02_大模型API调用/`：大模型 API 调用练习
- `MISSION.md`：学习任务目标
- `RESOURCES.md`：学习资源清单
- `NOTES.md`：教学偏好和过程记录

## 当前进度

- 已完成 Agent 基础概念
- 正在学习用 Python 调用大模型 API

## 在新环境继续学习

克隆仓库：

```bash
git clone https://github.com/ren997/agent-dev-learning.git
cd agent-dev-learning
```

安装 `teach` skill：

```bash
npx skills@latest add mattpocock/skills
```

这个命令会重新下载 `.agents/skills/`。该目录是本机 Agent 工具配置，已被 `.gitignore` 忽略，不提交到仓库。

继续学习时，可以在 Cursor 里说：

```text
/teach 继续教我 Agent 开发
```

即使没有安装 `teach` skill，也可以直接让 Agent 读取 `MISSION.md`、`NOTES.md`、`learning-records/` 和 `lessons/`，继续当前学习进度。

如果要运行第二节代码，复制配置文件：

```bash
copy 02_大模型API调用\config.example.json 02_大模型API调用\config.json
```

然后在 `config.json` 里填入自己的 API Key。

## 安全提醒

`02_大模型API调用/config.json` 用于本地保存 API Key，已被 `.gitignore` 忽略，不要提交到 Git。
