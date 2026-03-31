import streamlit as st  
# --- 核心要求：显示个人信息 --- 
st.set_page_config(page_title="我的 AI 助手", layout="wide")  
# 这里就是你要修改的前端界面 
st.sidebar.title("开发人员信息") 
st.sidebar.info("姓名：阙联强") 
st.sidebar.info("学号：423830120")  
# --- 核心要求：参数调整 --- st.sidebar.title("⚙️ AI 参数设置") 
temp = st.sidebar.slider("创造力权重 (Temperature)", 0.0, 1.0, 0.7) # 调整这个参数  
st.title("🤖 阙联强的ai聊天机器人") 
st.write("欢迎来到我的 AI 项目，本项目已实现基础迁移与前端优化。")  
# 模拟 AI 回复逻辑 if "messages" not in st.session_state:     
st.session_state.messages = []  
for message in st.session_state.messages:     
  with st.chat_message(message["role"]):         
    st.markdown(message["content"])  
if prompt := st.chat_input("想问点什么？"):     
  st.session_state.messages.append({"role": "user", "content": prompt})     
with st.chat_message("user"):         
  st.markdown(prompt)          
with st.chat_message("assistant"):         
  response = f"我是由[阙联强]开发的 AI。你刚才说的是：'{prompt}'。当前环境参数 Temperature 设为 {temp}。"         
  st.markdown(response)
  st.session_state.messages.append({"role": "assistant", "content": response})
