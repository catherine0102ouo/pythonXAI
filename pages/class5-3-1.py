import streamlit as st

st.chat_message("user").write("這是使用者訊息")
st.chat_message("assistant").write("這是AI的回應")

# 範例對話紀錄
history = [
    {"role": "user", "content": "你好，AI！"},
    {"role": "assistant", "content": "哈囉！有什麼我可以幫忙的嗎？"},
    {"role": "user", "content": "請問 st.chat_message() 怎麼用？"},
    {"role": "assistant", "content": "st.chat_message() 可以讓你用聊天泡泡的方式顯示訊息喔！"},
]   # Pin selection to current chat prompt(Ctrl+X)/Dont show this again(Alt+/)

#用迴圈顯示聊天泡泡
for message in history:
    if message["role"] == "user":
        st.chat_message("user",avatar="🪄").write(message["content"])
    else:
        st.chat_message("assistant",avatar="✨").write(message["content"])
        