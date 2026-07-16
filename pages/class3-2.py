import streamlit as st
import time

if st.button("重新整理", key="button1"):  # 如果按鈕被按下
    st.success("準備重新整理")  # 顯示綠色訊息
    time.sleep(3)  # 等待3秒
    st.rerun()  # 重新整理整個頁面

if "apple" not in st.session_state:  # 如果session_state中沒有apple這個變數
    st.session_state.apple = []

st.title("點餐機")
col1, col2 = st.columns(2)
with col1:
    a=st.text_input("請輸入餐點:")
with col2:
    if st.button("加入",key="button2"):
        st.session_state.apple.append(a)  # 將輸入的餐點加入session_state中的apple列表


st.title("購物籃")

for index, item in enumerate(st.session_state.apple):
    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(item)

    with col2:
        if st.button("刪除", key=f"delete_{index}"):
            st.session_state.apple.pop(index)
            st.rerun()   






