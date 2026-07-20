import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool  # 使用 @tool 装饰器
from datetime import datetime
import requests

# 1. 初始化模型
llm = ChatOpenAI(
    model="glm-4-flash",
    openai_api_key="48342d9cc3a74484884e8d5c97752f77.6MPxzYK0O6HTKcw8",  # 改成你的
    base_url="https://open.bigmodel.cn/api/paas/v4",
    temperature=0.7
)

# 2. 使用 @tool 装饰器定义工具函数
@tool
def get_current_time() -> str:
    """获取当前的日期和时间。"""
    return datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")

@tool
def get_weather() -> str:
    """查询聊城当前的天气情况。"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": 36.65, "longitude": 117.0, "current_weather": True}
    try:
        data = requests.get(url, params=params, timeout=5).json()
        temp = data["current_weather"]["temperature"]
        return f"聊城当前温度：{temp}°C"
    except:
        return "天气服务暂时不可用"

# 3. 创建 Agent（使用 create_agent）
# 根据你的版本，create_agent 可能接受 tools 列表和 system_prompt
agent = create_agent(
    model=llm,
    tools=[get_current_time, get_weather],
    system_prompt="你是一个有用的助手，必须使用工具来回答问题。"
)

# 4. Streamlit 界面
st.title("🤖 我的第一个 AI Agent")
user_input = st.text_input("输入你的问题：", "现在几点了？聊城天气怎么样？")

if st.button("发送"):
    with st.spinner("Agent 思考中..."):
        # 调用 Agent（输入格式可能是 {"messages": [...]}）
        result = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]}
        )
        # 提取最终回答
final_message = result["messages"][-1].content  # ✅ 正确
st.success("回答：")
st.write(final_message)