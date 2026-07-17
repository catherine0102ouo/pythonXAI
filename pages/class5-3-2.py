import streamlit as st

#初始化對話紀錄
if "history" not in st.session_state:
    st.session_state.history=[]

#顯示歷史紀錄
for message in st.session_state.history:
    st.chat_message("user",avatar="🪄").write(message["content"])

#聊天輸入框
Prompt = st.chat_input("請輸入訊息")
if Prompt:
    st.session_state.history.append({"content":Prompt,"role":"user"})
    st.rerun()#重新整理頁面顯示新訊息
