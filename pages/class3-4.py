import streamlit as st
import random

# 設定網頁標題與可愛的圖示
st.set_page_config(page_title="猜數字遊戲", page_icon="🎈")

st.title("猜數字遊戲 ( •̀ ω •́ )✧")

# 1. 初始化遊戲狀態與猜測範圍（預設 1 ~ 100）
if 'answer' not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
    st.session_state.min_val = 1
    st.session_state.max_val = 100
    st.session_state.game_over = False
    st.session_state.feedback = ""      # 用來存「太大」或「太小」的提示文字
    st.session_state.feedback_type = "" # 用來存提示的顏色類型 (error, warning, success)

# 2. 顯示上一次猜測的提示結果（如果有的話）
if st.session_state.feedback:
    if st.session_state.feedback_type == "error":
        st.error(st.session_state.feedback)
    elif st.session_state.feedback_type == "warning":
        st.warning(st.session_state.feedback)
    elif st.session_state.feedback_type == "success":
        st.success(st.session_state.feedback)

# 3. 動態顯示提示文字，會根據猜錯的結果更新範圍
input_label = f"請輸入 {st.session_state.min_val} ~ {st.session_state.max_val} 的數字："

# 建立輸入框（限定輸入範圍在目前縮小的範圍內）
guess = st.number_input(
    input_label, 
    min_value=st.session_state.min_val, 
    max_value=st.session_state.max_val, 
    step=1, 
    value=st.session_state.min_val  # 預設值設為當前最小值
)

# 4. 建立送出答案按鈕
if st.button("送出答案"):
    if st.session_state.game_over:
        st.info("遊戲已經結束囉！請點擊下方的「重新開始」按鈕。")
    else:
        # 用你學過的 if-elif-else 判斷大小，並同步更新範圍與提示！
        if guess > st.session_state.answer:
            st.session_state.feedback = f"【{guess}】太大了！ 📈"
            st.session_state.feedback_type = "error"
            st.session_state.max_val = guess - 1 # 猜太大，縮小上限
            st.rerun()  # 重新整理畫面，更新範圍與顯示提示
            
        elif guess < st.session_state.answer:
            st.session_state.feedback = f"【{guess}】太小了！ 📉"
            st.session_state.feedback_type = "warning"
            st.session_state.min_val = guess + 1 # 猜太小，放大下限
            st.rerun()  # 重新整理畫面，更新範圍與顯示提示
            
        else:
            st.session_state.feedback = "答對了！！！ 恭喜你！ 🎉🎉🎉"
            st.session_state.feedback_type = "success"
            st.session_state.game_over = True
            st.balloons() # 答對放氣球！！！
            st.rerun()

# 5. 重新開始按鈕（要把所有範圍重設回 1~100）
if st.button("重新開始"):
    st.session_state.answer = random.randint(1, 100)
    st.session_state.min_val = 1
    st.session_state.max_val = 100
    st.session_state.game_over = False
    st.session_state.feedback = ""
    st.session_state.feedback_type = ""
    st.rerun()