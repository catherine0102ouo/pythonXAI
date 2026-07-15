# Python 入門筆記（國中生版）

---

# 第一章：Python 是什麼？

Python 是一種**程式語言**，可以讓我們寫程式，請電腦幫我們完成工作，例如：

- 計算數學
- 製作遊戲
- 製作網站
- 分析資料
- 製作 AI

---

# 第二章：輸出文字 `print()`

`print()` 可以把內容顯示在畫面上。

### 範例

```python
print("Hello World")
```

輸出：

```
Hello World
```

也可以輸出自己的名字：

```python
print("Catherine")
```

---

## 換行符號 `\n`

`\n` 代表**換到下一行**。

```python
print("不要低頭\n雙下巴會出來")
```

輸出：

```
不要低頭
雙下巴會出來
```

---

# 第三章：註解（Comment）

註解是給人看的說明，**Python 不會執行**。

## 單行註解

在前面加上 `#`

```python
# 這是一行註解
print("Hello")
```

---

## 多行註解

使用三個雙引號 `""" """`

```python
"""
這是第一行
這是第二行
這是第三行
"""
```

---

### 小技巧

在 VS Code 中：

```
Ctrl + /
```

可以快速註解或取消註解。

---

# 第四章：Python 的基本資料型態

程式中的資料有不同種類。

| 型態  | 名稱           | 範例        |
| ----- | -------------- | ----------- |
| int   | 整數           | 1、100、-5  |
| float | 浮點數（小數） | 3.14、1.5   |
| str   | 字串（文字）   | "apple"     |
| bool  | 布林值         | True、False |

---

## 整數（int）

```python
print(10)
```

輸出：

```
10
```

---

## 小數（float）

```python
print(3.14)
```

輸出：

```
3.14
```

---

## 字串（str）

文字一定要加引號。

```python
print("apple")
```

---

## 布林值（bool）

只有兩種結果：

```python
True
False
```

通常代表：

- True＝是、成功、正確
- False＝否、失敗、錯誤

例如：

```python
print(True)
print(False)
```

---

# 第五章：`len()` 計算長度

`len()` 可以算出字串有幾個字。

```python
print(len("apple"))
```

輸出：

```
5
```

因為：

```
a p p l e
1 2 3 4 5
```

再例如：

```python
print(len(","))
```

輸出：

```
1
```

---

# 第六章：`type()` 查看資料型態

可以知道資料屬於哪一種型態。

```python
print(type(1))
```

輸出：

```
<class 'int'>
```

其他例子：

```python
print(type(1.0))
```

```
<class 'float'>
```

```python
print(type("apple"))
```

```
<class 'str'>
```

```python
print(type(True))
```

```
<class 'bool'>
```

---

# 第七章：資料型態轉換

有時候需要把資料改成另一種型態。

## 轉成整數 `int()`

```python
print(int(1.9))
```

輸出：

```
1
```

**注意：**
小數轉整數會直接去掉小數部分，不會四捨五入。

---

## 轉成小數 `float()`

```python
print(float(5))
```

輸出：

```
5.0
```

---

## 轉成字串 `str()`

```python
print(str(100))
```

輸出：

```
100
```

（變成文字）

---

## 轉成布林值 `bool()`

```python
print(bool(1))
```

輸出：

```
True
```

通常：

```
0 → False
其他數字 → True
```

---

### 不能亂轉換！

例如：

```python
int("hello")
```

會出現錯誤。

因為：

```
"hello"
```

不是數字。

---

# 第八章：讓使用者輸入資料 `input()`

可以請使用者輸入內容。

```python
name = input("請輸入名字：")
```

如果輸入：

```
小明
```

變數 `name` 就會存著：

```
小明
```

---

## 為什麼常常要加 `float()`？

因為：

```python
input()
```

得到的是**文字（字串）**。

如果要做數學運算，就要轉成數字。

例如：

```python
age = float(input("請輸入年齡："))
```

---

# 第九章：變數（Variable）

變數就像一個**盒子**，可以存放資料。

例如：

```python
score = 100
```

表示：

```
score
┌──────┐
│100   │
└──────┘
```

之後就可以一直使用。

---

# 第十章：f 字串（格式化輸出）

使用：

```python
f"文字 {變數}"
```

例如：

```python
name = "小明"

print(f"你好，{name}")
```

輸出：

```
你好，小明
```

---

# 第十一章：計算圓面積

公式：

```
圓面積 = π × 半徑²
```

Python：

```python
r = float(input("請輸入半徑："))

print(f"圓面積為：{3.14 * r ** 2}")
```

說明：

- `**` 表示次方
- `r**2` 就是 `r × r`

例如：

半徑：

```
5
```

結果：

```
圓面積為：78.5
```

---

# 第十二章：計算平均成績

```python
chinese_mid = float(input("請輸入國文期中成績："))
chinese_final = float(input("請輸入國文期末成績："))

print(f"國文平均成績為：{(chinese_mid + chinese_final) / 2}")
```

例如：

```
期中：90
期末：80
```

結果：

```
國文平均成績為：85.0
```

---

# 第十三章：Streamlit（做網頁）

Streamlit 是一個可以用 Python 快速製作**簡單網頁**的工具。

先匯入：

```python
import streamlit as st
```

其中：

- `import`：匯入套件
- `streamlit`：套件名稱
- `st`：簡寫，之後可以直接使用 `st`

---

# 第十四章：`st.title()`

建立最大標題。

```python
st.title("這是標題")
```

畫面：

```
這是標題
========
```

---

# 第十五章：`st.write()`

最常用的顯示方式。

```python
st.write("Hello")
```

可以顯示：

- 文字
- 數字
- 表格
- Markdown
- 圖片
- 很多其他資料

---

# 第十六章：`st.text()`

只能顯示**純文字**。

```python
st.text("Hello")
```

沒有任何特殊格式。

---

# 第十七章：`st.markdown()`

可以使用 Markdown 語法，讓畫面更漂亮。

例如：

```python
st.markdown("""
# 第一層標題

## 第二層標題

### 第三層標題

- 第一項
- 第二項
- 第三項

---
""")
```

可以製作：

- 大標題
- 小標題
- 粗體
- 斜體
- 清單
- 分隔線
- 程式碼區塊

---

# 今天學到的重要指令整理

| 指令                     | 功能                         |
| ------------------------ | ---------------------------- |
| `print()`                | 顯示文字或結果               |
| `#`                      | 單行註解                     |
| `""" """`                | 多行註解                     |
| `len()`                  | 計算字串長度                 |
| `type()`                 | 查看資料型態                 |
| `int()`                  | 轉成整數                     |
| `float()`                | 轉成小數                     |
| `str()`                  | 轉成字串                     |
| `bool()`                 | 轉成布林值                   |
| `input()`                | 讓使用者輸入資料             |
| `f"{}"`                  | 格式化輸出文字               |
| `**`                     | 次方運算                     |
| `import streamlit as st` | 匯入 Streamlit 套件          |
| `st.title()`             | 建立標題                     |
| `st.write()`             | 顯示內容（最常用）           |
| `st.text()`              | 顯示純文字                   |
| `st.markdown()`          | 使用 Markdown 製作格式化內容 |

---

# 本日重點總結

今天學會了 Python 最基本的觀念，包括：

1. 使用 `print()` 顯示內容。
2. 認識四種基本資料型態：`int`、`float`、`str`、`bool`。
3. 使用 `len()` 和 `type()` 查看資料資訊。
4. 使用 `int()`、`float()`、`str()`、`bool()` 做資料型態轉換。
5. 使用 `input()` 接收使用者輸入，並搭配變數儲存資料。
6. 利用 `f"{}"` 讓輸出內容更容易閱讀。
7. 能撰寫簡單的程式，例如計算圓面積和平均成績。
8. 初步認識 Streamlit，知道如何用 `st.title()`、`st.write()`、`st.text()` 和 `st.markdown()` 製作簡單的網頁介面。
