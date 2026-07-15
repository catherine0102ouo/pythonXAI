print("Hello World")
print("Catherine")
print("不要低頭\n雙下巴會出來")
"""
這是多行註解
"""
#這是單行註解
print("Hello World!")#print是在終端機顯示文字的指令
#ctrl+?可以快速註解/取消註解
#基本型態
print(1)#int這是整數,-1,0,1,2,3,4,5,6,7,8,9
print(1,0)#float這是浮點數
print(1,234)#float這是浮點數
print("apple")#str這是字串"sadasd123125557",'1'
print(True)#bool這是布林值True/False
print(False)#bool這是布林值True/False

print(len("apple"))#len()是一個函式,可以計算字串的長度
print(len(","))#len()是一個函式,可以計算字串的長度
#type()#可以查看變數的型態
print(type(1))#<class 'int'>
print(type(1.0))#<class 'float'>
print(type("apple"))#<class 'str'>
print(type(True))#<class 'bool'>

#型態轉換
print(int(1.0))#float轉int
print(float(1))#int轉float
print(str(1))#int轉str
print(bool(1))#int轉bool
print(int(1.234))#float轉int
print(float("1.234"))#str轉floats
print(str(1.234))#float轉str
print(bool(1.234))#float轉bool
#print(int("hello"))#這行會報錯,因為字串裡面如果有非數字的字元,無法轉換成數字

#請使用者輸入半徑,計算園面積
r=float(input("請輸入半徑:"))
print(f"圓面積為:{3.14*r**2}")
#向使用者詢問國文的期中成績,期末成績,輸出平均成績
請輸入國文期中成績:90
請輸入國文期末成績:80
chinese_mid=float(input("請輸入國文期中成績:"))
chinese_final=float(input("請輸入國文期末成績:"))
print(f"國文平均成績為:{(chinese_mid+chinese_final)/2}")


