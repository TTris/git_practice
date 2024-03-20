# module -> 就是一個python的檔案。 使用方法把寫好的功能弄成一包工具包

# #使用 import
# import day_4
# #記得 "." 功能
# bmi = day_4.get_bmi(180.3, 57)
# print(bmi)
# print(day_4.test)

# Search Python documentation for existing module

# import random
#
# # below is test 1
#
# coin = random.randint(0, 1)
# if coin == 0:
#     print("正面")
# else:
#     print("反面")

#============================================

# list
# 中括號 []
# 取得列表中的某數, 從0開始算!!!!
#         0   1   2   3   4
#        -5   -4  -3  -2  -1
# score = [15, True, 35, "你好哇", 68, 68, 68, 68]
# print(score[1])
# print(score[-1])
# print(score[-2])
# # print(score[8])  #會跑出error: out of range!
#
# #要延伸列表，可用 ".append" (只能加一個）
# score.append(653)
# print(score)
# score.append([12, 11, 10])  #這個就是巢狀列表 nested list
# print(score)
# print(score[-1])
# print(score[-1][-1])
#
# #想知道某值在列表裡出現幾次 -> count
# count_num = score.count(68)
# print(count_num)
#
# #search python documentation>list(資料結構) for more list functions.
#====================================



#below is test 2
# import random
# # foods = ["拉麵", "串燒", "貓咪", "牛肉麵", "雞排", "羊肉爐", "空氣"]
# # food = random.randint(0,6)
# #
# # print(f"今晚吃{foods[food]}")
#
# print("歡迎使用今晚吃什麼？")
# what_to_eat = input("請輸入晚餐選項（中間請用逗號隔開）")
# foods = what_to_eat.split(",")
# food = random.randint(0,len(foods)-1)
# print(f"今晚吃{foods[food]}")

# ".split" & "len()" 都是問chatGPT的呦！

#==============================================

#nest list巢狀列表
# num = [
#     [2, 3, 77],
#     [5, "Hi", 53],
#     ["you", 98, 77]
# ]
# 二維列表通常儲存平面資訊（地址）

# =========== below is project 5=================
import random
users_input = input("剪刀！石頭！布！請輸入字母剪刀(S)、石頭(R)、布(P)").upper()
computers_input = random.randint(0,2)

def users_game():
    if users_input == "S":
        return 0
    elif users_input == "R":
        return 1
    elif users_input == "P":
        return 2
    else:
        return 100

def user_image():
    if users_game() == 0:
        return "✂️"
    elif users_game() == 1:
        return "🪨"
    elif users_game() == 2:
        return "🖐🏻"
    else:
        return "了個鳥🐥"

def computers_game():
    if computers_input == 0:
        return 0
    elif computers_input == 1:
        return 1
    else:
        return 2

def computer_image():
    if computers_game() == 0:
        return "✂️"
    elif computers_game() == 1:
        return "🪨"
    else:
        return "🖐🏻"

def result(user_num, computer_num):
    if user_num == computer_num:
        return "平手"
    elif user_num - computer_num == 1 or user_num - computer_num == -2:
        return "恭喜你贏了！"
    elif user_num - computer_num == -1 or user_num - computer_num == 2:
        return "哇～輸了"
    else:
        return "不要亂出！"


print(f"你出{user_image()}")
print(f"電腦出{computer_image()}")
print(f"結果是：{result(user_num=users_game(), computer_num=computers_game())}")

#S=0, R=1, P=2


#====below is solutions from teacher===============
# scissor = '''
#      _____
# ____   ____)___
#     ___________)
#     ___________)
#     (______)
# ----(___)
# '''
#
# rock = '''
#         _____
# _______(________)
#         (________)
#        (_________)
#        (_______)
# ------(______)
#       '''
#
# paper = '''
#     _____
# ____   ____)___
#     ___________)
#     ___________)
#     (__________)
# ----(_________)
# '''
# import random
#
# options = ["s", "r", "p"]
# user_choice = input("請輸入字母Ｓ(剪刀)、Ｒ(石頭)、Ｐ(布)").upper()
# computer_choice = options[random.randint(0,2)]
#
# print("你出：")
# if user_choice == "S":
#     print(scissor)
# elif user_choice == "R":
#     print(rock)
# else:
#     print(paper)
#
# print("電腦出：")
# if computer_choice == "s":
#     print(scissor)
# elif computer_choice == "r":
#     print(rock)
# else:
#     print(paper)
#
#
# if (user_choice == "S" and computer_choice == "p") or \
#    (user_choice == "R" and computer_choice == "s") or \
#    (user_choice == "P" and computer_choice == "r"):
#     print("恭喜你贏了")
# elif (user_choice == "S" and computer_choice == "s") or \
#      (user_choice == "R" and computer_choice == "r") or \
#      (user_choice == "P" and computer_choice == "p"):
#     print("平手")
# else:
#     print("你輸了QQ")

