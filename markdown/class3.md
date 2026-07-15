# Python 學習筆記（第 3 天）

---

# Python 學習筆記（第 3 天）

## Streamlit：欄位（Columns）、文字輸入、Session State

今天學到如何使用 **Streamlit** 製作更有互動性的網頁，包括欄位排版、文字輸入、按鈕，以及如何讓程式記住資料。

---

# 一、欄位（Columns）

## 什麼是欄位？

欄位（Columns）可以把網頁畫面分成好幾個區域，讓元件可以**左右排列**，而不是全部由上往下排列。

---

## 建立兩個欄位

```python
import streamlit as st

col1, col2 = st.columns(2)
```

代表畫面平均分成兩個欄位。

可以在不同欄位放不同元件：

```python
col1.button("按鈕1")
col2.button("按鈕2")
```

畫面效果：

```
┌────────────┬────────────┐
│  按鈕1     │   按鈕2    │
└────────────┴────────────┘
```

---

## 設定欄位寬度

除了平均分配，也可以設定每個欄位的比例。

```python
col1, col2 = st.columns([1,2])
```

表示：

```
col1 : col2

 1   :   2
```

第二欄會比第一欄寬兩倍。

---

## 建立三個欄位

```python
col1, col2, col3 = st.columns([1,2,3])
```

代表畫面分成三欄，比例依序是：

```
1 : 2 : 3
```

---

# 二、with 的用法

如果同一個欄位裡要放很多元件，可以使用 `with`。

例如：

```python
with col1:
    st.button("按鈕")
    st.write("這是第一欄")
```

代表縮排內的所有程式，都會顯示在第一欄。

另一欄也可以：

```python
with col2:
    st.button("按鈕2")
    st.write("這是第二欄")
```

這樣程式會更整齊，也比較容易閱讀。

---

# 三、按鈕（Button）

建立按鈕：

```python
st.button("按我一下")
```

如果按下按鈕，就會回傳 `True`。

例如：

```python
if st.button("按我"):
    st.write("你按下按鈕了！")
```

只有按下按鈕時，才會顯示文字。

---

## 氣球動畫

```python
if st.button("按我"):
    st.balloons()
```

按下按鈕後，畫面會出現氣球動畫。

> **注意**
>
> 你的程式中寫的是：
>
> ```python
> st.ballons()
> ```
>
> 正確拼法應該是：
>
> ```python
> st.balloons()
> ```

---

# 四、利用 for 建立多個欄位

建立四個欄位：

```python
cols = st.columns(4)
```

接著利用迴圈建立按鈕：

```python
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}")
```

畫面會出現：

```
按鈕1    按鈕2    按鈕3    按鈕4
```

使用迴圈可以減少重複程式碼。

---

# 五、Columns 排列方式比較

## 方法一：先建立欄位，再放很多元件

```python
col1, col2 = st.columns(2)
```

第一欄：

```
按鈕1
按鈕2
按鈕3
```

第二欄：

```
文字1
文字2
文字3
```

每一欄都是由上往下排列。

---

## 方法二：每次迴圈重新建立欄位

```python
for i in range(3):
    col1, col2 = st.columns(2)
```

畫面變成：

```
按鈕1   文字1

按鈕2   文字2

按鈕3   文字3
```

每一列都是新的兩欄配置。

---

# 六、文字輸入（text_input）

讓使用者輸入文字。

```python
text = st.text_input("請輸入文字")
```

也可以設定預設內容：

```python
text = st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

顯示輸入結果：

```python
st.write(f"你輸入的文字是{text}")
```

---

# 七、Session State（狀態保存）

## 一般變數

例如：

```python
ans = 1

if st.button("加一"):
    ans += 1

st.write(ans)
```

第一次按：

```
2
```

第二次按：

```
2
```

而不是：

```
3
```

### 為什麼？

因為 Streamlit 每按一次按鈕，就會重新執行整個程式。

所以：

```python
ans = 1
```

每次都會重新開始。

---

## Session State

Session State 可以把資料暫時儲存在程式中，即使重新執行，資料也不會消失。

建立資料：

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1
```

按下按鈕：

```python
if st.button("加一"):
    st.session_state.ans1 += 1
```

顯示：

```python
st.write(st.session_state.ans1)
```

執行結果：

```
第一次：2
第二次：3
第三次：4
```

---

## 建立新的 Session State

例如：

```python
if "apple" not in st.session_state:
    st.session_state.apple = 1
```

就建立了一個名為 `apple` 的資料，可以在整個程式中持續使用。

---

# 八、重新執行程式（rerun）

有時候畫面不會立刻更新，可以使用：

```python
st.rerun()
```

例如：

```python
if st.button("重新整理畫面"):
    st.rerun()
```

按下按鈕後，整個程式會重新執行一次，畫面也會更新。

---

# 本日重點整理

| 指令                | 功能                           |
| ------------------- | ------------------------------ |
| `st.title()`        | 建立網頁標題                   |
| `st.columns()`      | 建立欄位                       |
| `st.columns([1,2])` | 設定欄位寬度比例               |
| `with col:`         | 在指定欄位放置多個元件         |
| `st.button()`       | 建立按鈕                       |
| `st.balloons()`     | 顯示氣球動畫                   |
| `st.text_input()`   | 建立文字輸入框                 |
| `value=`            | 設定預設文字                   |
| `st.session_state`  | 保存資料，不會因重新執行而消失 |
| `st.rerun()`        | 重新執行整個程式               |

---

# 📌 今天一定要記住的 5 個重點

1. **`st.columns()` 可以把畫面切成多個欄位，讓元件左右排列。**
2. **使用 `with col:` 可以在同一個欄位放多個元件，程式也會更整齊。**
3. **`st.text_input()` 可以建立文字輸入框，`value=` 可以設定預設文字。**
4. **一般變數每次重新執行程式都會重設，但 `st.session_state` 可以保存資料。**
5. **`st.rerun()` 可以強制重新執行程式，讓畫面更新到最新狀態。**
