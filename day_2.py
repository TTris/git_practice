# data type 資料型態

# 1. string -> "whatever it is." 單引號 or 雙引號都可以
# 取得字串中的特定文字 "你好小白" [0] 要用中括號！
# name = "你好小白"
# print (name[0] + name[3])
# input 得到的值皆為string

# 若想在字串中加入 ""
# print ("他今年\"25\"歲")

# 若想在字串中換行 \n
#print ("Hi,\nhow are you")

# 字串中執行其他資料型態 -> f-string {} 字串前加f, 變數加{}
# age = 30
# height = 150.9
# is_male = True
# print(f"我今年{age}歲，身高{height}。是否為男性：{is_male}。")




# 2. int -> 整數 integer
# 數字加上底線，方便閱讀且不影響資料型態
# num1 = 100_000_000
# num2 = 300_000
# print (num1 + num2)

# 整數除法 (去餘數) //
# print (33//10)

# 取餘數 %
# print(100 % 9)

# Orders:
# ()
# ** //
# * / %
# + -
# 不知道順序就找Thonny

# 四捨五入 -> round (值, 要取到小數點後第幾位)
# print(round(1000/3, 2))

# num = 10
# num = num + 1
# # 也可寫成 num += 1
# num = num * 3
# # 也可寫成 num *= 3


# 3. float -> 有小數點的數值



# 4. boolean -> 邏輯 True or False (True = 1, False = 0)





# type () -> 判斷資料型態

# below is test 1
# num = input("請輸入一個兩位數數字：")
# num1 = int(num[0])
# num2 = int(num[1])
# print(num1 + num2)




# below is project 2

# height = input("請輸入您的身高（公分）：\n")
# weight = input("請輸入您的體重（公斤）：\n")
#
# height = float(height) / 100
# weight = float(weight)
#
# BMI = round(weight / height ** 2, 1)
#
# print(f"您的BMI是{BMI}")
