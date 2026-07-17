# Python + Streamlit + OpenAI 課程筆記(第五天)

---

# 第1章：圖片元件（Image）

## 1. 載入套件

```python
import streamlit as st
import os
```

### 說明

- `streamlit`：建立網頁介面。
- `os`：管理資料夾與檔案。

---

## 2. 顯示標題

```python
st.title("圖片元件")
```

效果：

```
圖片元件
=========
```

---

## 3. 顯示圖片

```python
st.image("image/apple.png", width=300)
```

### 說明

- `st.image()`：顯示圖片。
- `width`：設定圖片寬度。

例如：

```python
st.image("cat.png", width=200)
```

代表圖片寬度是200像素。

---

## 4. 取得資料夾所有圖片

```python
image_folder = "image"
image_files = os.listdir(image_folder)
```

### 說明

假設資料夾：

```
image
│
├── apple.png
├── banana.png
├── orange.png
```

執行後

```python
image_files
```

會得到

```python
['apple.png', 'banana.png', 'orange.png']
```

---

## 5. 顯示所有檔名

```python
st.write(image_files)
```

畫面會出現

```
apple.png
banana.png
orange.png
```

---

## 6. number_input（數字輸入）

```python
image_size = st.number_input(
    "圖片大小",
    min_value=50,
    max_value=500,
    step=50,
    value=100
)
```

### 常用參數

| 參數      | 功能         |
| --------- | ------------ |
| min_value | 最小值       |
| max_value | 最大值       |
| step      | 每次增加多少 |
| value     | 預設值       |

例如：

```
圖片大小

100
```

使用者可以調整：

50 →100→150→200……

---

## 7. for 顯示全部圖片

```python
for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)
```

### 流程

```
apple.png
↓

顯示圖片

↓

banana.png

↓

顯示圖片

↓

orange.png

↓

顯示圖片
```

---

## 8. use_container_width

```python
st.image(
    "apple.png",
    use_container_width=True
)
```

代表：

圖片會自動填滿目前容器的寬度。

通常比固定寬度更漂亮。

---

## 9. 成功訊息

```python
st.success("購買成功！")
```

畫面會出現綠色提示。

還有：

```python
st.error()
```

錯誤訊息（紅色）

```python
st.warning()
```

警告（黃色）

```python
st.info()
```

資訊（藍色）

---

# 第2章 Session State（記住資料）

## 為什麼需要 Session State？

一般 Streamlit：

按按鈕

↓

整頁重新整理

↓

所有變數重新開始

所以要使用：

```python
st.session_state
```

保存資料。

---

## 建立購物車

```python
if "cart" not in st.session_state:
    st.session_state.cart = {}
```

代表：

第一次進來

↓

建立空購物車。

---

## 建立商品資料

```python
st.session_state.products = {
    "蘋果":{
        "price":45,
        "stock":10
    }
}
```

商品資料包含：

- 價格
- 庫存
- 圖片

---

# 第3章 Streamlit 網頁排版

## 1. 設定網頁

```python
st.set_page_config(
    page_title="商城",
    page_icon="🛍️",
    layout="wide"
)
```

可以設定：

- 標題
- 網頁圖示
- 寬版模式

---

## 2. columns（欄位）

```python
col1,col2 = st.columns(2)
```

畫面：

```
左邊 │ 右邊
```

也可以：

```python
st.columns([7,3])
```

代表：

```
70%    30%
```

---

## 3. container（容器）

```python
with st.container(border=True):
```

作用：

把內容包成一個方框。

---

## 4. caption（小字）

```python
st.caption("歡迎光臨")
```

適合顯示說明文字。

---

## 5. markdown

```python
st.markdown("---")
```

畫水平線。

也可以顯示 Markdown 語法。

---

# 第4章 按鈕(Button)

## 一般按鈕

```python
if st.button("加入購物車"):
```

按下才會執行。

---

## 停用按鈕

```python
st.button(
    "已售完",
    disabled=True
)
```

按鈕不能按。

---

## Primary Button

```python
st.button(
    "立即結帳",
    type="primary"
)
```

主要按鈕會比較醒目。

---

# 第5章 購物車功能

## 加入購物車

流程：

```
按下加入

↓

庫存-1

↓

加入購物車

↓

重新整理畫面
```

---

## 刪除商品

```
按下➖

↓

購物車數量-1

↓

庫存+1

↓

數量=0

↓

刪除商品
```

---

## 計算總金額

```python
subtotal = 價格 × 數量
```

最後：

```
total_amount
```

就是全部商品總價。

---

## 結帳

```python
st.balloons()
```

會放氣球動畫。

接著：

```python
st.success()
```

顯示成功訊息。

---

# 第6章 檔案處理

## 檢查資料夾是否存在

```python
os.path.exists(image_folder)
```

存在：

```
True
```

不存在：

```
False
```

---

## 建立資料夾

```python
os.makedirs(image_folder)
```

建立新的資料夾。

---

## 組合路徑

```python
os.path.join(folder,file)
```

例如：

```
image

+

apple.png

↓

image/apple.png
```

---

# 第7章 上傳圖片

```python
uploaded_image = st.file_uploader(
    "上傳圖片",
    type=["png","jpg","jpeg"]
)
```

只能上傳：

- png
- jpg
- jpeg

---

## 儲存圖片

```python
with open(...,"wb") as f:
```

把圖片寫進資料夾。

其中：

```python
getbuffer()
```

取得圖片資料。

---

# 第8章 OpenAI API

## 載入套件

```python
import openai
from dotenv import load_dotenv
```

---

## 載入 .env

```python
load_dotenv()
```

讀取

```
.env
```

裡面的 API 金鑰。

---

## 設定 API Key

```python
openai.api_key = os.getenv(
    "OPENAI_API_KEY"
)
```

或

```python
st.secrets["OPENAI_API_KEY"]
```

---

## 建立聊天

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...]
)
```

### 重要參數

| 參數     | 功能     |
| -------- | -------- |
| model    | AI模型   |
| messages | 對話內容 |

---

## 取得 AI 回答

```python
assistant_message =
response.choices[0].message.content
```

---

# 第9章 AI 對話紀錄

## messages

格式：

```python
messages = [
    {
        "role":"system",
        "content":"..."
    },
    {
        "role":"user",
        "content":"你好"
    },
    {
        "role":"assistant",
        "content":"哈囉"
    }
]
```

---

## 三種角色

### system

設定 AI 的規則。

例如：

```
請全部使用繁體中文
```

---

### user

使用者說的話。

---

### assistant

AI 的回答。

---

## 加入新的訊息

```python
messages.append(...)
```

例如：

```python
messages.append({
    "role":"user",
    "content":"你好"
})
```

---

# 第10章 Chat 元件

## 顯示聊天泡泡

```python
st.chat_message("user")
```

使用者泡泡。

```python
st.chat_message("assistant")
```

AI泡泡。

---

## 自訂頭像

```python
avatar="🪄"
```

例如：

```python
st.chat_message(
    "user",
    avatar="🪄"
)
```

---

## chat_input

```python
prompt = st.chat_input(
    "請輸入訊息"
)
```

會在畫面最下方出現聊天輸入框。

---

# 第11章 AI 聊天機器人流程

完整流程：

```
使用者輸入

↓

加入 history

↓

送到 OpenAI

↓

AI回答

↓

加入 history

↓

重新整理

↓

全部聊天重新顯示
```

---

# 第12章 AI 設定

## 修改 System Message

```python
st.text_input()
```

可以改變 AI 的個性，例如：

```
請當數學老師
```

或

```
請用英文回答
```

---

## 選擇模型

```python
st.selectbox()
```

例如：

```
gpt-4o-mini

gpt-4o

gpt-4o-search-preview
```

讓使用者自由切換模型。

---

## 清空聊天

```python
st.session_state.history = []
```

刪除所有聊天紀錄。

---

# 第13章 今天學到的重要指令整理

| 指令                               | 功能                       |
| ---------------------------------- | -------------------------- |
| `st.image()`                       | 顯示圖片                   |
| `os.listdir()`                     | 取得資料夾內所有檔案       |
| `st.number_input()`                | 數字輸入框                 |
| `st.success()`                     | 成功訊息                   |
| `st.warning()`                     | 警告訊息                   |
| `st.error()`                       | 錯誤訊息                   |
| `st.info()`                        | 資訊訊息                   |
| `st.columns()`                     | 分欄排版                   |
| `st.container()`                   | 建立容器                   |
| `st.button()`                      | 按鈕                       |
| `st.chat_message()`                | 聊天泡泡                   |
| `st.chat_input()`                  | 聊天輸入框                 |
| `st.file_uploader()`               | 上傳檔案                   |
| `st.selectbox()`                   | 下拉選單                   |
| `st.text_input()`                  | 文字輸入框                 |
| `st.session_state`                 | 儲存資料，不因重新整理消失 |
| `st.rerun()`                       | 重新整理頁面               |
| `st.toast()`                       | 跳出小通知                 |
| `st.balloons()`                    | 放氣球動畫                 |
| `os.path.exists()`                 | 檢查檔案或資料夾是否存在   |
| `os.makedirs()`                    | 建立資料夾                 |
| `os.path.join()`                   | 合併檔案路徑               |
| `load_dotenv()`                    | 載入 `.env` 設定檔         |
| `os.getenv()`                      | 讀取環境變數               |
| `openai.chat.completions.create()` | 呼叫 OpenAI API            |
| `messages.append()`                | 新增對話紀錄               |

---

# 本日重點總整理

今天主要學會了五個重要主題：

1. **圖片元件**：學會使用 `st.image()` 顯示圖片，利用 `os.listdir()` 讀取資料夾中的所有圖片，並搭配 `st.number_input()` 動態調整圖片大小。
2. **購物商城實作**：利用 `st.session_state` 保存商品與購物車資料，搭配 `st.columns()`、`st.container()`、`st.button()` 等元件，完成商品展示、加入購物車、結帳及後台庫存管理功能。
3. **檔案與圖片管理**：學會使用 `os.path.exists()`、`os.makedirs()`、`os.path.join()` 管理資料夾，並利用 `st.file_uploader()` 上傳圖片並儲存到指定位置。
4. **OpenAI API 串接**：學會透過 `load_dotenv()` 或 `st.secrets` 載入 API 金鑰，使用 `openai.chat.completions.create()` 呼叫 AI 模型，並取得 AI 回覆內容。
5. **AI 聊天機器人**：學會使用 `st.chat_message()`、`st.chat_input()` 建立聊天介面，利用 `messages` 與 `st.session_state.history` 保存完整對話紀錄，並加入系統訊息、模型切換及清空聊天等功能，完成一個可持續對話的 AI 聊天機器人。
