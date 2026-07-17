import streamlit as st
with st.expander("Class1課堂筆記"):
    st.write(
    """
# Python 入門筆記

---

# 第一章：Python 是什麼？

Python 是一種**程式語言**，可以讓我們寫程式，請電腦幫我們完成工作，例如：

* 計算數學
* 製作遊戲
* 製作網站
* 分析資料
* 製作 AI

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
\"""
這是第一行
這是第二行
這是第三行
\"""
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

| 型態    | 名稱      | 範例         |
| ----- | ------- | ---------- |
| int   | 整數      | 1、100、-5   |
| float | 浮點數（小數） | 3.14、1.5   |
| str   | 字串（文字）  | "apple"    |
| bool  | 布林值     | True、False |

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

* True＝是、成功、正確
* False＝否、失敗、錯誤

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

* `**` 表示次方
* `r**2` 就是 `r × r`

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

* `import`：匯入套件
* `streamlit`：套件名稱
* `st`：簡寫，之後可以直接使用 `st`

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

* 文字
* 數字
* 表格
* Markdown
* 圖片
* 很多其他資料

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
st.markdown(\"""
# 第一層標題

## 第二層標題

### 第三層標題

- 第一項
- 第二項
- 第三項

---
\""")
```

可以製作：

* 大標題
* 小標題
* 粗體
* 斜體
* 清單
* 分隔線
* 程式碼區塊

---

# 今天學到的重要指令整理

| 指令                       | 功能                  |
| ------------------------ | ------------------- |
| `print()`                | 顯示文字或結果             |
| `#`                      | 單行註解                |
| `""" """`                | 多行註解                |
| `len()`                  | 計算字串長度              |
| `type()`                 | 查看資料型態              |
| `int()`                  | 轉成整數                |
| `float()`                | 轉成小數                |
| `str()`                  | 轉成字串                |
| `bool()`                 | 轉成布林值               |
| `input()`                | 讓使用者輸入資料            |
| `f"{}"`                  | 格式化輸出文字             |
| `**`                     | 次方運算                |
| `import streamlit as st` | 匯入 Streamlit 套件     |
| `st.title()`             | 建立標題                |
| `st.write()`             | 顯示內容（最常用）           |
| `st.text()`              | 顯示純文字               |
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
"""

    )
with st.expander("Class2課堂筆記"):
    st.write(
    """# Python 學習筆記（第 2 天）

---

# 一、比較運算子（Comparison Operators）

比較運算子是用來**比較兩個值是否符合條件**，結果只會有兩種：

- `True`（真）
- `False`（假）

> ⚠️ 注意：通常要比較**相同資料型態**（例如數字跟數字、文字跟文字）。

| 運算子 | 意思     | 範例   | 結果  |
| ------ | -------- | ------ | ----- |
| `==`   | 等於     | `1==1` | True  |
| `!=`   | 不等於   | `1!=1` | False |
| `>`    | 大於     | `5>3`  | True  |
| `<`    | 小於     | `3<5`  | True  |
| `>=`   | 大於等於 | `5>=5` | True  |
| `<=`   | 小於等於 | `3<=5` | True  |

### 範例

```python
print(5 > 3)
```

輸出：

```
True
```

---

# 二、邏輯運算子（Logical Operators）

當我們有**兩個以上條件**要一起判斷時，就會使用邏輯運算子。

---

## 1. and（而且）

只有**全部都是真**，結果才是真。

| 條件A | 條件B | 結果  |
| ----- | ----- | ----- |
| True  | True  | True  |
| True  | False | False |
| False | True  | False |
| False | False | False |

### 記法

> **有一個 False，就全部 False。**

範例：

```python
print(5>3 and 10>8)
```

結果：

```
True
```

---

## 2. or（或者）

只要**其中一個是真**，結果就是真。

| 條件A | 條件B | 結果  |
| ----- | ----- | ----- |
| True  | True  | True  |
| True  | False | True  |
| False | True  | True  |
| False | False | False |

### 記法

> **只要有一個 True，就是 True。**

---

## 3. not（不是）

把結果相反。

```python
print(not True)
```

結果

```
False
```

```python
print(not False)
```

結果

```
True
```

---

# 三、運算優先順序

Python 會依照固定順序計算。

| 優先順序 | 運算                      |
| -------- | ------------------------- |
| 1        | `()` 括號                 |
| 2        | `**` 次方                 |
| 3        | `* / // %`                |
| 4        | `+ -`                     |
| 5        | 比較運算子 (`== > < ...`) |
| 6        | `not`                     |
| 7        | `and`                     |
| 8        | `or`                      |

### 小技巧

> **有括號先算括號！**

---

# 四、if、elif、else 條件判斷

根據不同條件執行不同程式。

語法：

```python
if 條件:
    程式

elif 條件:
    程式

else:
    程式
```

---

### 密碼判斷

```python
password=input("請輸入密碼:")

if password=="1234":
    print("歡迎Jeffrey")

elif password=="5678":
    print("歡迎Tim")

elif password=="0000":
    print("歡迎Chloe")

else:
    print("密碼錯誤")
```

---

## if 和 elif 的差別

### 多個 if

每個 if 都會檢查。

```python
if ...
if ...
if ...
```

即使第一個符合，後面還是會繼續判斷。

---

### if + elif + else

```python
if ...
elif ...
elif ...
else ...
```

找到符合條件後，就不再往下判斷。

✅ 比較快、效率比較好。

---

# 五、Streamlit 基本功能

Streamlit 可以把 Python 程式變成網頁。

先匯入：

```python
import streamlit as st
```

---

## 1. number_input()

讓使用者輸入數字。

```python
number = st.number_input(
    "請輸入整數",
    step=1,
    min_value=0,
    max_value=100
)
```

常用設定：

- `step=1`：一次增加 1（只能輸入整數）
- `min_value`：最小值
- `max_value`：最大值

---

## 2. markdown()

在網頁顯示文字。

```python
st.markdown("Hello")
```

也可以顯示變數：

```python
st.markdown(f"你輸入的是 {number}")
```

---

## 3. 成績判斷

```python
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
```

---

## 4. button()

建立按鈕。

```python
st.button("按我一下")
```

如果按下：

```python
if st.button("按我"):
    print("按下了")
```

---

## 5. 氣球效果

```python
if st.button("按我"):
    st.balloons()
```

按下後會出現🎈動畫。

> ⚠️ 原始程式寫成 `st.ballons()`，正確拼法是 **`st.balloons()`**（有兩個 **o**）。

---

# 六、for 迴圈

for 用來**重複做事情**。

基本寫法：

```python
for i in range(5):
    print(i)
```

輸出

```
0
1
2
3
4
```

---

## range()

### ① 一個數字

```python
range(5)
```

代表：

```
0 1 2 3 4
```

---

### ② 起點、終點

```python
range(1,5)
```

代表：

```
1 2 3 4
```

---

### ③ 起點、終點、間隔

```python
range(1,10,2)
```

代表：

```
1 3 5 7 9
```

---

## 注意

range() **不包含最後一個數字。**

---

# 七、九九乘法（三角形）

```python
number = st.number_input(...)

for i in range(1,number+1):
    st.write(str(i)*i)
```

假設輸入

```
5
```

結果

```
1
22
333
4444
55555
```

因為

```python
str(i)*i
```

代表把文字重複很多次。

---

# 八、List（串列）

List 可以一次存很多資料。

建立：

```python
L=[1,2,3]
```

也可以混合型態：

```python
L=[1,True,"Hello",3.14]
```

---

## 讀取元素

Index（索引）從 **0** 開始。

```python
L=["a","b","c"]

print(L[0])
```

輸出：

```
a
```

---

# 九、List 切片（Slice）

格式：

```python
L[開始:結束:間隔]
```

例如：

```python
L=[1,2,3,"a","b","c"]

print(L[1:4])
```

結果：

```
[2,3,'a']
```

因為：

- 包含開始
- 不包含結束

---

每隔一個取：

```python
print(L[::2])
```

結果

```
[1,3,'b']
```

---

# 十、List 常用功能

## append()

新增元素。

```python
L=[1,2,3]

L.append(4)
```

結果

```
[1,2,3,4]
```

---

## remove()

移除指定內容。

```python
L=["a","b","c"]

L.remove("a")
```

只會刪掉第一個符合的。

---

## pop()

依照位置刪除。

```python
L.pop(0)
```

刪除第一個。

```python
L.pop()
```

刪除最後一個。

---

## sort()

排序。

```python
L=[3,1,5,2]

L.sort()
```

結果：

```
[1,2,3,5]
```

預設是由小排到大。

---

# 十一、走訪 List

有兩種方式。

---

## 方法一：利用 Index

```python
for i in range(len(L)):
    print(L[i])
```

適合需要知道位置。

---

## 方法二：直接取元素

```python
for item in L:
    print(item)
```

適合只需要資料，不需要知道索引。

---

# 本日重點整理

| 主題         | 重點                               |
| ------------ | ---------------------------------- |
| 比較運算子   | 比較兩個值，結果只有 True 或 False |
| 邏輯運算子   | `and`、`or`、`not` 用來組合條件    |
| if 判斷      | 根據不同條件執行不同程式           |
| elif         | 找到符合條件後，不再繼續判斷       |
| Streamlit    | 可以快速做出互動式網頁             |
| number_input | 讓使用者輸入數字                   |
| markdown     | 在網頁顯示文字                     |
| button       | 建立按鈕                           |
| balloons     | 顯示氣球動畫                       |
| for          | 重複執行程式                       |
| range        | 產生一段數字範圍（不包含結束值）   |
| List         | 一次存放多筆資料                   |
| append       | 新增元素                           |
| remove       | 刪除指定元素                       |
| pop          | 刪除指定位置元素                   |
| sort         | 排序 List                          |
| Slice        | 使用 `開始:結束:間隔` 取出部分資料 |
| List 走訪    | 可用索引或直接取得元素             |

---

## 📚 今天一定要記住的 5 個重點

1. **比較運算子的結果一定是 `True` 或 `False`。**
2. **`if → elif → else` 找到符合條件後就不會再往下判斷。**
3. **`for + range()` 是 Python 最常用的迴圈。**
4. **List 的索引（Index）從 `0` 開始。**
5. **`append()` 新增、`remove()` 刪指定值、`pop()` 刪指定位置、`sort()` 排序，是 List 最常用的四個功能。**
""")
with st.expander("Class3課堂筆記"):

    st.write(
    """# Python 學習筆記（第 3 天）

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
""")
with st.expander("Class4課堂筆記"):

    st.write(
    """# Python 與 Streamlit 課堂筆記

## 一、什麼是 Streamlit？

Streamlit 是一個可以快速把 Python 程式變成網頁的工具。

### 匯入模組

```python
import streamlit as st
import time
import random
```

- `import`：匯入外部功能。
- `streamlit`：製作網頁介面。
- `time`：控制時間。
- `random`：產生隨機數字。

---

# 二、Streamlit 常用元件

## 1. 網頁標題

```python
st.title("點餐機")
```

顯示大標題。

---

## 2. 按鈕

```python
st.button("加入")
```

建立一個按鈕。

搭配 `if` 使用：

```python
if st.button("加入"):
    print("按鈕被按下")
```

---

## 3. 輸入框

```python
a = st.text_input("請輸入餐點")
```

讓使用者輸入文字。

---

## 4. 數字輸入框

```python
guess = st.number_input("請輸入數字")
```

只能輸入數字。

---

## 5. 顯示訊息

```python
st.success("成功")
st.warning("警告")
st.error("錯誤")
st.info("提示")
```

不同顏色代表不同訊息。

---

## 6. 分欄

```python
col1, col2 = st.columns(2)
```

將畫面分成兩欄。

```python
with col1:
    st.write("左邊")

with col2:
    st.write("右邊")
```

---

## 7. 重新整理頁面

```python
st.rerun()
```

重新執行整個程式。

---

# 三、session_state（記住資料）

平常 Streamlit 每次按按鈕都會重新執行程式。

如果想保留資料，可以使用：

```python
st.session_state
```

### 建立資料

```python
if "apple" not in st.session_state:
    st.session_state.apple = []
```

意思：

如果還沒有 apple 這個資料，就建立空串列。

---

### 新增資料

```python
st.session_state.apple.append(a)
```

加入餐點。

---

### 刪除資料

```python
st.session_state.apple.pop(index)
```

刪除指定位置資料。

---

# 四、點餐機範例

流程：

1. 輸入餐點
2. 按「加入」
3. 存到購物籃
4. 顯示所有餐點
5. 可以按「刪除」

### enumerate()

```python
for index, item in enumerate(list1):
```

同時取得：

- index（編號）
- item（內容）

例如：

```python
水果 = ["蘋果","香蕉","橘子"]

for index,item in enumerate(水果):
    print(index,item)
```

結果：

```
0 蘋果
1 香蕉
2 橘子
```

---

# 五、算術指定運算子

## 一般寫法

```python
a = a + 1
```

## 簡寫

```python
a += 1
```

---

| 運算子 | 意思   |
| ------ | ------ |
| +=     | 加     |
| -=     | 減     |
| \*=    | 乘     |
| /=     | 除     |
| //=    | 取商   |
| %=     | 取餘數 |
| \*\*=  | 次方   |

範例：

```python
a = 5

a += 3
print(a)
```

結果：

```
8
```

---

# 六、運算優先順序

由高到低：

```text
1. ()
2. **
3. * / // %
4. + -
5. == != > < >= <=
6. not
7. and
8. or
9. = += -= *= /= ...
```

例如：

```python
3 + 2 * 5
```

先算：

```python
2 * 5
```

得到：

```python
13
```

---

# 七、while 迴圈

## 基本格式

```python
while 條件:
    程式碼
```

只要條件成立就會一直執行。

範例：

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

結果：

```
0
1
2
3
4
```

---

# 八、break

可以強制結束迴圈。

```python
for i in range(5):
    if i == 3:
        break

    print(i)
```

結果：

```
0
1
2
```

到 3 就停止。

---

# 九、random 隨機數

## 匯入

```python
import random
```

---

## randrange()

```python
random.randrange(7)
```

結果：

```
0~6
```

隨機選一個。

---

```python
random.randrange(1,6)
```

結果：

```
1~5
```

---

```python
random.randrange(1,6,2)
```

可能得到：

```
1
3
5
```

---

## randint()

```python
random.randint(1,100)
```

結果：

```
1~100
```

兩端都包含。

---

# 十、猜數字遊戲

## 遊戲流程

1. 電腦產生答案
2. 玩家猜數字
3. 顯示太大或太小
4. 自動縮小範圍
5. 猜中後結束遊戲

---

例如答案是：

```
22
```

第一次猜：

```
50
```

顯示：

```
50太大了
```

範圍變：

```
1 ~ 49
```

---

再猜：

```
10
```

顯示：

```
10太小了
```

範圍變：

```
11 ~ 49
```

這樣可以幫助玩家更快找到答案。

---

# 十一、字典（Dictionary）

## 什麼是字典？

字典是一種：

```text
key → value
(鍵 → 值)
```

的資料結構。

例如：

```python
d = {
    "a":1,
    "b":2,
    "c":3
}
```

---

## 取得資料

```python
print(d["a"])
```

結果：

```
1
```

---

# 十二、取得 key、value

## keys()

取得所有鍵

```python
d.keys()
```

結果：

```python
dict_keys(['a','b','c'])
```

---

## values()

取得所有值

```python
d.values()
```

結果：

```python
dict_values([1,2,3])
```

---

## items()

取得鍵和值

```python
d.items()
```

結果：

```python
('a',1)
('b',2)
('c',3)
```

---

# 十三、新增與修改字典

## 新增

```python
d["d"] = 4
```

結果：

```python
{
'a':1,
'b':2,
'c':3,
'd':4
}
```

---

## 修改

```python
d["a"] = 5
```

結果：

```python
{
'a':5,
'b':2,
'c':3,
'd':4
}
```

---

# 十四、刪除資料

## pop()

```python
d.pop("a")
```

刪除 a 並回傳其值。

---

如果不存在：

```python
d.pop("e","not found")
```

結果：

```python
not found
```

---

# 十五、in 的用法

檢查 key 是否存在。

```python
"a" in d
```

結果：

```python
True
```

---

```python
"e" in d
```

結果：

```python
False
```

---

# 十六、巢狀字典（字典裡面放字典）

範例：

```python
grade = {
    "小明":{
        "國文":[90,80,70],
        "數學":[85,75,65]
    }
}
```

---

取得數學成績：

```python
grade["小明"]["數學"]
```

結果：

```python
[85,75,65]
```

---

# 十七、平均數計算

## 平均公式

```python
平均 = 總和 ÷ 個數
```

---

### sum()

加總

```python
sum([90,80,70])
```

結果：

```python
240
```

---

### len()

計算數量

```python
len([90,80,70])
```

結果：

```python
3
```

---

### 平均

```python
avg = sum(scores) / len(scores)
```

---

# 十八、課程重點總整理

今天學到的重要觀念：

✅ Streamlit 製作網頁介面
✅ 按鈕、輸入框、欄位配置
✅ session_state 保存資料
✅ 點餐機與購物籃功能
✅ 算術指定運算子（+=、-=）
✅ while 迴圈
✅ break 跳出迴圈
✅ random 隨機數
✅ 猜數字遊戲製作
✅ Dictionary（字典）
✅ key、value、items 的使用
✅ 字典新增、修改、刪除
✅ 巢狀字典資料結構
✅ sum()、len() 計算平均成績

這些內容已經包含了 **Python 基礎程式設計 + Streamlit 網頁互動 + 資料結構(Dictionary)** 的重要入門觀念，是製作小型網頁遊戲和資料管理系統的基礎。


""")
with st.expander("Class5課堂筆記"):
    
    st.write(
    """# Python + Streamlit + OpenAI 課程筆記(第五天)

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


""")    