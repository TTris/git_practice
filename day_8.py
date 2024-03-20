# 變數作用域： 全域變數  、  區域變數
#       global variable, local variable

# 函數的內部 -> 區域變數
# def abc(a,b):
#     c = a + b
#     print(c)
#
# abc(1, 2)
# # 直接在外面print(c)是 not defined
# # print(c)
#
# #在外部的變數 -> 全域變數
# e = 10
#
# print(e)




# 在函數內部更改全域變數

a = 1

#===========用global的方式 ！不推薦！ 容易出錯 ＆ 出錯難除==========
# def abc():
#     global a  #告訴電腦目前要修改的a是全域變數
#     a = 2
#     print(f"函數內部：{a}")
#
# abc()
# print(f"函數外部：{a}")

#=================可使用return的方式, 較推薦=====================
# def abc():
#     print(f"函數內部：{a}")
#     return 2
#
# a = abc()
# print(f"函數外部：{a}")
#

#========below is test 1 =============
#
#
# Q1 = """
# def fun1(a,b):
#     c = a + b
#     return c
#
# fun1(10, 20)
# print(c)
# """
#
# Q2 = """
# x = 5
# def fun2():
#     x = 50
#     return x
#
# fun2()
# print(x)
# """
#
# Q3 = """
# x = 10
# def fun3():
#     global x
#     x = 50
#     if 2 > 1:
#         x = 100
#     return x
#
# fun3()
# print(x)
# """


#====================
# 迴圈用法 break, continue


# break:

# for i in range(1, 6):
#     print(i)
#
# print("跳出迴圈")
#
#
# for i in range(1, 6):
#     print(i)
#     if i == 3:
#         break
#
# print("跳出迴圈")
#
# i = 1
# while i < 6:
#     print(i)
#     if i == 2:
#         break
#     i += 1
#
# print("跳出迴圈")

# highest = 0
# for score in [20, 30, 60, 100, 20, 100, 50, 30]:
#     print(score)
#     if score == 100:
#         highest = 100
#         break
#
#     if score > highest:
#         highest = score
#
# print(f"最高分{highest}")


# continue -> 直接進入下一次迴圈，不執行下方的程式碼

# highest = 0
# for score in [20, 30, 60, 100, 20, 100, 50, 30]:
#     if score == 30:
#         continue
#     print(score)
#
# i = 1
# while i < 6:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1


#=====below is project 8==================
import random

print("歡迎來到猜數字遊戲！\n"
      "謎底為1-100的隨機整數\n"
      "最多5次機會！來猜猜😄\n")

i = 1
game_ans = random.randint(1, 100)

while i < 6:
    print(f"第{i}次猜測")
    guess = (input("請輸入猜測的數字："))
    try:
        guess = int(guess)
    except:
        print("請輸入整數")
        i += 1
        continue
    guess = int(guess)
    if guess == game_ans:
        print("恭喜你猜對了！🥳")
        break
    elif guess < game_ans:
        if i == 5:
            print(f"挑戰失敗，謎底是{game_ans}😄")
            break
        print("猜高一點⬆️\n")
        i += 1
    else:
        if i == 5:
            print(f"挑戰失敗，謎底是{game_ans}😄")
            break
        print("猜低一點⬇️\n")
        i += 1

#===========below is solution from teacher=================
# import random
#
# print("歡迎來到猜數字遊戲！\n"
#       "謎底為1-100的隨機整數\n"
#       "最多5次機會！來猜猜😄\n")
#
# guess_num = 0
# random_number = random.randint(0, 101)
#
# while True:
#     guess_num += 1
#     if guess_num >= 6:
#         print("你輸了！超出猜測次數")
#         print(f"謎底是：{random_number}")
#         break
#     print(f"第{guess_num}次猜測")
#     user_guess = input("請輸入猜測的數字：")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#     else:
#         print("只能輸入整數")
#         continue
#     if user_guess > random_number:
#         print("低一點")
#     elif user_guess < random_number:
#         print("高一點")
#     else:
#         print("恭喜猜對")
#         break
