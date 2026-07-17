# Python 與 Streamlit 課堂筆記(第四天)

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
