# ai-agent-demo
# 🤖 多工具 AI Agent 对话系统

基于 LangChain 1.x + Streamlit + 智谱 GLM-4-Flash 构建的多工具 AI Agent。

## 功能

- 查询当前日期和时间
- 查询聊城实时天气
- Agent 自动判断调用哪个工具
- 支持多工具协同回答

## 技术栈

- LangChain 1.3.14
- Streamlit
- 智谱 GLM-4-Flash API
- Python 3.x

## 运行步骤

1. 创建虚拟环境
```bash
python -m venv .venv
.venv\Scripts\activate
2.安装依赖

bash
pip install langchain langchain-openai streamlit requests
3.修改 API Key
在 agent_web.py 第 9 行替换你的智谱 API Key

4.运行

bash
streamlit run agent_web.py
