import streamlit as st #匯入streamlit模組並重新命名為st

#st.number_input()可以讓使用者輸入數字,設定step=1可以讓使用者只能輸入整數
#min_value=0可以設定最小值為0,max_value=100可以設定最大值為100
number = st.number_input("請輸入一個整數", step=1, min_value=0, max_value=100)
#st.markdown()可以在網頁使用markdown語法顯示文字
st.markdown(f"你輸入的數字是: {number}")

st.markdown("使用者輸入成績")
st.markdown("### 練習")
number = st.number_input("請輸入你的分數",step=1, min_value=0, max_value=100)
if number>=90:
    st.markdown("A")
elif number>=80:
    st.markdown("B")
elif number>=70:
    st.markdown("C")
elif number>=60:
    st.markdown("D")
else:
    st.markdown("F")
import streamlit as st #匯入streamlit模組並重新命名為st

st.markdown("---")
st.markdown("### 按鈕練習")
# st.button()可以在網頁上顯示一個按鈕,使用者可以點及按鈕
#key是按鈕的識別名稱,可以用來區分不同的按鈕
#如果使用者點擊按鈕,st.button()會回傳True,否則回傳False
st.button("按我一下",key="button1")
if st.button("按我一下",key="ballons"):
    st.ballons()
if st.button("按我一下",key="snow"):
    st.markdown("---")