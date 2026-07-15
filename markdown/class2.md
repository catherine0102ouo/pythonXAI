# Python 學習筆記（第 2 天）

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
