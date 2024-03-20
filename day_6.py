# 越越打的：swd1q                               ````````

# while loop -> 重複執行一段程式碼直到為False

#sample 1
# i = 1
#
# while i < 6:
#     print(87)
#     i += 1
#
# print("程式結束")

#sample 2
# name = input("猜猜我是誰？")
#
# while name != "小芝":
#     print("答錯惹！再猜看看")
#     name = input("猜猜我是誰？")
#
# print("答對了！")

# below is test 1

# again = "Y"
#
# while again == "Y":
#     height = input("請輸入您的身高（公分）：\n")
#     weight = input("請輸入您的體重（公斤）：\n")
#
#     height = float(height) / 100
#     weight = float(weight)
#
#     BMI = round(weight / height ** 2, 1)
#     print(f"您的BMI是{BMI}")
#     again = input("請問還要再計算嗎？(Y/N)").upper()
#
#
# print("感謝使用")
#


#=========================
# for loop 取出字串or列表中的每一個字  for __ in ， 取完之後跳出迴圈  -> 記得冒號

# for item in "我是小白":
#     print("進入迴圈")
#     print(item)
#
# print("程式結束")
#
# for number in [25, 36, 77, 698]:
#     print(f"你{number}幾歲")
#
# print("end")

# scores = [80, 60, 50, 30, 100, 80, 50, 100, 30, 50]
#
# plus = 0
#
# for score in scores:  #小白老師說，通常是 for 單數 in 複數  eg. for num in nums
#     plus = score + plus  # plus += score
#
# print(plus)


# below is test 2

# nums = input("請輸入學生成績(請用逗號「,」隔開)")
# nums_list = nums.split(",")
# max = 0
# for num in nums_list:
#     num = int(num)
#     if max >= num:
#         max = max
#     else:
#         max = num
#
# print(f"最高分的是{max}")


#below is solution from teacher
# scores_str = input("請輸入學生成績(請用逗號「,」隔開)\n")
# scores = scores_str.split(",")
#
# highest_score = 0
# for score in scores:
#     if int(score) > highest_score:
#         highest_score = int(score)
# print(f"最高分的是：{highest_score}")

#========================
# range ()
# for i in range(1, 11): #(從1~11) 不包含11.
#     print(i)
# for ii in range(1, 10, 3): #第三個參數為間隔
#     print(ii)

# sum_i = 0
# for i in range(1, 101):
#     sum_i += i
# print(sum_i)


#below is test 3

# sum = 0
# for i in range (0, 101, 2):
#     sum += i
# print(sum)

#teacher has 2 solutions. 1 is like above (mine) the other's like below
# sum = 0
# for i in range (1, 101):
#     if i%2 == 0:
#         sum += i
# print(sum)


#==============below is project 6 ============
import random

letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]


print("歡迎使用密碼產生器")
nums_upper = int(input("請問需要幾個大寫字母？"))
nums_lower = int(input("請問需要幾個小寫字母？"))
nums_num = int(input("請問需要幾個數字？"))
nums_symbol = int(input("請問需要幾個符號？"))

# i = 0
# while i < nums_upper:
#     upper_letter = letters_upper[random.randint(0, 25)]
#     print(upper_letter, end='')
#     i += 1
#
# i = 0
# while i < nums_lower:
#     lower_letter = letters_lower[random.randint(0, 25)]
#     print(lower_letter, end='')
#     i += 1
#
# i = 0
# while i < nums_num:
#     nums = numbers[random.randint(0, 9)]
#     print(nums, end='')
#     i += 1
#
# i = 0
# while i < nums_symbol:
#     symbol = symbols[random.randint(0, 9)]
#     print(symbol, end='')
#     i += 1

#=====below is solution from teacher========

passwords = ""
for i in range(0, nums_upper):
    passwords += letters_upper[random.randint(0, 25)]
#     passwords += " "  #為了advanced版本加的（原本沒有）

for i in range(0, nums_lower):
    passwords += letters_lower[random.randint(0, 25)]
#    passwords += " "  #為了advanced版本加的（原本沒有）

for i in range(0, nums_num):
    passwords += numbers[random.randint(0, 9)]
#     passwords += " "  #為了advanced版本加的（原本沒有）

for i in range(0, nums_symbol):
    passwords += symbols[random.randint(0, 9)]
#     passwords += " "  #為了advanced版本加的（原本沒有）

print(passwords)

#====below is advanced version=======

# passwords = passwords.split()
# password = ""
#
# for i in range(0, len(passwords)):
#     password = random.sample(passwords, len(passwords))
#
# password = "".join(password)
# print(password)


#====below is solutions from teacher for advanced version===========

password_list = list(passwords)
random.shuffle(password_list)  #shuffle不需要給一個變數，會直接變
new_password = ""

for chr in password_list:
    new_password += chr
print(new_password)


