import streamlit as st
import os

# 1. 初始化 session_state 狀態，確保資料在頁面重整時不會消失
if "cart" not in st.session_state:
    st.session_state.cart = {}

# 模擬商品與庫存資料庫
if "products" not in st.session_state:
    st.session_state.products = {
        "新鮮紅蘋果": {"price": 45, "stock": 10, "image": "apple.png"},
        "香甜熟香蕉": {"price": 35, "stock": 5, "image": "banana.png"},
        "多汁鮮柳丁": {"price": 40, "stock": 1, "image": "orange.png"}
    }

st.set_page_config(page_title="單頁式直覺購物平台", page_icon="🛍️", layout="wide")

# 設定圖片資料夾
image_folder = "image"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# ==========================================
# 區塊一：前台商城購物頁面 (最上方)
# ==========================================
st.title("🛍️ 歡迎光臨 線上購物商城")
st.caption("✨ 購物與庫存管理一頁搞定，直接往下捲動即可進入後台")

# 建立主畫面左右區塊：左邊 70% 放商品，右邊 30% 放購物車
main_col, cart_col = st.columns([7, 3], gap="large")

# --- 左側：商品展示區 ---
with main_col:
    st.header("📦 熱銷商品目錄")
    
    if not st.session_state.products:
        st.warning("目前商城內沒有任何商品，請滾動至網頁下方新增商品！")
    else:
        # 在主畫面內再切分 3 欄網格排版商品
        prod_cols = st.columns(3)
        
        for idx, (prod_name, details) in enumerate(st.session_state.products.items()):
            col = prod_cols[idx % 3]
            image_path = os.path.join(image_folder, details["image"])
            
            with col:
                # 使用 container 框住商品，更有卡片感
                with st.container(border=True):
                    st.subheader(prod_name)
                    
                    # 檢查圖片是否存在
                    if os.path.exists(image_path):
                        st.image(image_path, use_container_width=True)
                    else:
                        st.caption("⚠️ 暫無商品圖片 (請至下方後台上傳)")
                        
                    st.markdown(f"單價：**${details['price']}** 元")
                    
                    # 顯示庫存與購買按鈕
                    current_stock = details["stock"]
                    if current_stock > 0:
                        st.markdown(f"剩餘庫存：`{current_stock}` 件")
                        if st.button(f"➕ 加入購物車", key=f"add_{prod_name}"):
                            # 扣減庫存
                            st.session_state.products[prod_name]["stock"] -= 1
                            # 加入購物車
                            if prod_name in st.session_state.cart:
                                st.session_state.cart[prod_name]["quantity"] += 1
                            else:
                                st.session_state.cart[prod_name] = {"price": details["price"], "quantity": 1}
                            st.toast(f"已將 {prod_name} 放進購物車！", icon="🛒")
                            st.rerun()
                    else:
                        st.markdown("剩餘庫存：❌ `已售完`")
                        st.button("🚫 已售完", key=f"disabled_{prod_name}", disabled=True)

# --- 右側：購物車與結帳區 ---
with cart_col:
    with st.container(border=True):
        st.header("🛒 我的購物車")
        st.markdown("---")
        
        if not st.session_state.cart:
            st.write("您的購物車目前是空的 😢")
        else:
            total_amount = 0
            for prod_name, info in list(st.session_state.cart.items()):
                subtotal = info["price"] * info["quantity"]
                total_amount += subtotal
                
                c_item, c_btn = st.columns([3, 1])
                with c_item:
                    st.write(f"**{prod_name}**")
                    st.caption(f"${info['price']} x {info['quantity']} = ${subtotal}")
                with c_btn:
                    # 減少數量按鈕（退還庫存）
                    if st.button("➖", key=f"remove_{prod_name}"):
                        st.session_state.cart[prod_name]["quantity"] -= 1
                        st.session_state.products[prod_name]["stock"] += 1
                        
                        if st.session_state.cart[prod_name]["quantity"] <= 0:
                            del st.session_state.cart[prod_name]
                        st.rerun()
            
            st.markdown("---")
            st.subheader(f"總金額：${total_amount} 元")
            
            # 結帳按鈕
            if st.button("💳 立即結帳", type="primary", use_container_width=True):
                st.balloons()
                st.success(f"🎉 購買成功！本次消費總共 ${total_amount} 元！")
                st.session_state.cart = {}
                st.rerun()

# ==========================================
# 強烈的分隔線：區隔前台與後台
# ==========================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 區塊二：後台庫存管理頁面 (網頁最下方)
# ==========================================
st.title("⚙️ 商城後台庫存管理系統")
st.caption("🔒 此區域通常供管理員進行商品上架、下架與即時庫存補貨變更")

# 左右排版：左邊新增商品，右邊調整庫存
manage_left, manage_right = st.columns([4, 6], gap="large")

with manage_left:
    st.header("➕ 上架新商品")
    with st.form("add_product_form", clear_on_submit=True):
        new_name = st.text_input("商品名稱", placeholder="例如：大湖草莓")
        new_price = st.number_input("設定單價 (元)", min_value=1, max_value=10000, value=50, step=5)
        new_stock = st.number_input("初始庫存數量", min_value=0, max_value=999, value=10, step=1)
        
        uploaded_image = st.file_uploader("上傳商品圖片", type=["png", "jpg", "jpeg"])
        submit_btn = st.form_submit_button("🚀 確認上架商品", use_container_width=True)
        
        if submit_btn:
            if not new_name.strip():
                st.error("請輸入正確的商品名稱！")
            elif new_name in st.session_state.products:
                st.error("此商品名稱已存在！")
            else:
                image_filename = "default.png"
                if uploaded_image is not None:
                    image_filename = uploaded_image.name
                    with open(os.path.join(image_folder, image_filename), "wb") as f:
                        f.write(uploaded_image.getbuffer())
                
                st.session_state.products[new_name] = {
                    "price": new_price,
                    "stock": new_stock,
                    "image": image_filename
                }
                st.success(f"🎉 成功上架：{new_name}！")
                st.rerun()

with manage_right:
    st.header("📊 現有商品庫存盤點")
    
    if not st.session_state.products:
        st.info("目前還沒有任何商品資料。")
    else:
        for prod_name, details in list(st.session_state.products.items()):
            with st.container(border=True):
                col_info, col_edit, col_del = st.columns([3, 3, 1])
                
                with col_info:
                    st.write(f"**{prod_name}**")
                    st.caption(f"單價: ${details['price']} 元 | 圖片: {details['image']}")
                with col_edit:
                    new_stock_val = st.number_input(
                        f"調整庫存", 
                        min_value=0, 
                        max_value=999, 
                        value=details["stock"], 
                        key=f"edit_stock_{prod_name}",
                        label_visibility="collapsed" # 隱藏標籤讓畫面乾淨
                    )
                    st.session_state.products[prod_name]["stock"] = new_stock_val
                with col_del:
                    if st.button("🗑️", key=f"delete_{prod_name}"):
                        del st.session_state.products[prod_name]
                        if prod_name in st.session_state.cart:
                            del st.session_state.cart[prod_name]
                        st.rerun()











 