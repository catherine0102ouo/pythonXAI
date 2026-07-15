import streamlit as st
number = st.number_input("請輸入一個整數(1到9)", step=1, min_value=1, max_value=9)
for i in range(1,number+1):
    st.write(str(i)*i)