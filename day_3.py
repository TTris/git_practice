# if statement

# 記得冒號 : !!!


# is_raining = False
# if is_raining:
#     print ("drive to work")
# else:
#     print ("walk to work")



# score = 30
# if score >= 60:
#     print ("吃好料！")
# else:
#     print ("罰跪！")


# name = "林鮭魚"
# if name == "林鮭魚":
#     print("free!")
# else:
#     print("給錢")


# below is test 1

# num = int(input("請輸入一個整數\n"))
# if num % 2 == 1:
#     print("奇數")
# else:
#     print("偶數")


# elif (否則如果), nested if (巢狀 if)

# score = int(input("你考幾分呀？"))
# cheat = input("老師，他有作弊嗎？(Y/N)")
#
# if score >= 90:
#     if cheat == "Y" or cheat == "y":
#         print("還敢作弊！")
#     else:
#         print("我給你100元")
# elif score >= 80:
#     if cheat == "Y" or cheat == "y":
#         print("還敢作弊！")
#     else:
#         print("我給你50元")
# elif score >= 70:
#     if cheat == "Y" or cheat == "y":
#         print("還敢作弊！")
#     else:
#         print("我給你30元")
# else:
#     print("你欠我100元，去罰跪！")

# below is test two
# height = float(input("請輸入您的身高（公分）\n")) / 100
# weight = float(input("請輸入您的體重（公斤）\n"))
#
# bmi = round(weight / height ** 2, 1)
# judge = ""
#
# if bmi <= 18.5:
#     judge = "體重過輕"
# elif bmi < 24:
#     judge = "正常體位"
# elif bmi < 27:
#     judge = "體重過重，重一點而已，還好"
# elif bmi < 30:
#     judge = "輕度肥胖，已是肥了"
# elif bmi < 35:
#     judge = "中度肥胖，唉"
# elif bmi >= 35 :
#     judge = "你已胖到不行"
#
# print(f"您的BMI是：{bmi} ({judge})")


# 邏輯運算 (and, or, not)




# below is project 3
# print("歡迎使用拉麵點餐機～\n"
#       "(1) 鹽味拉麵 $220 \n"
#       "(2) 醬油拉麵 $240 \n"
#       "(3) 豚骨拉麵 $280")
#
# order = int(input("請選擇拉麵口味（輸入:1/2/3)"))
# plus = input("是否加大？豚骨+$50，其他口味+$30 (輸入：Y/N)").upper()
# egg = input("是否加溏心蛋+$30？(輸入：Y/N)").upper()
# meat = input("是否加叉燒+$60？(輸入：Y/N)").upper()
#
# total = 0
#
# if order == 1:
#     total += 220
#     if plus == "Y":
#         total += 30
#     elif plus == "N":
#         total += 0
#     else:
#         print("請不要亂選謝謝！")
#     if egg == "Y":
#         total += 30
#     elif egg == "N":
#         total += 0
#     else:
#         print("請不要亂選謝謝！")
#     if meat == "Y":
#         total += 60
#     elif meat == "N":
#         total += 0
#     else:
#         print("請不要亂選謝謝！")
#     if plus == "Y" and egg == "Y" and meat == "Y":
#         total -= 30
#         print(f"加好加滿折價$30，總金額{total}，感謝您的光臨！")
#     elif plus == "N" or egg == "N" or meat == "N":
#         print(f"總金額${total}，感謝您的光臨！")
#     else:
#         print("請你不要亂選謝謝")
# elif order == 2:
#     total += 240
#     if plus == "Y":
#         total += 30
#     elif plus == "N":
#         total += 0
#     else:
#         print("請不要亂選謝謝！")
#     if egg == "Y":
#         total += 30
#     elif egg == "N":
#         total += 0
#     else:
#         print("請不要亂選謝謝！")
#     if meat == "Y":
#         total += 60
#     elif meat == "N":
#         total += 0
#     else:
#         print("請不要亂選謝謝！")
#     if plus == "Y" and egg == "Y" and meat == "Y":
#         total -= 30
#         print(f"加好加滿折價$30，總金額{total}，感謝您的光臨！")
#     elif plus == "N" or egg == "N" or meat == "N":
#         print(f"總金額${total}，感謝您的光臨！")
#     else:
#         print("請你不要亂選謝謝")
# elif order == 3:
#     total += 280
#     if plus == "Y":
#         total += 50
#     elif plus == "N":
#         total += 0
#     else:
#         print("請不要亂選謝謝！")
#     if egg == "Y":
#         total += 30
#     elif egg == "N":
#         total += 0
#     else:
#         print("請不要亂選謝謝！")
#     if meat == "Y":
#         total += 60
#     elif meat == "N":
#         total += 0
#     else:
#         print("請不要亂選謝謝！")
#     if plus == "Y" and egg == "Y" and meat == "Y":
#         total -= 30
#         print(f"加好加滿折價$30，總金額${total}，感謝您的光臨！")
#     elif plus == "N" or egg == "N" or meat == "N":
#         print(f"總金額${total}，感謝您的光臨！")
#     else:
#         print("請你不要亂選謝謝")
# else:
#     print("請你不要亂選謝謝")
#

