# function 函數 （函式）
# search "python documentation" for python build-in function list

# use "def" to build function. 一定要做縮排!! 要有冒號!!
# def print_info():
#     print("小白今年24歲")
#     print("小白身高179公分")
#
# print_info()


# def print_info(name, age, height):
#     print(f"{name}今年{age}歲")
#     print(f"{name}身高{height}公分")
#
# name = input("請輸入你的名字")
#
# # 參數值若不想按照順序寫，就要指定參數！ 如下
# print_info(name, height=166, age= 25)

# below is test 1

# def find_max(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         print(num1)
#     elif num2 >= num1 and num2 >= num3:
#         print(num2)
#     else:
#         print(num3)
#
# find_max(-50,150,30)


# 函數回傳 return
# 函數若沒有回傳值，就是return None
# 函數遇到 return 就會執行回傳，不會執行下面的程序

# def find_max(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# # 這樣才是print function return的值
# print(find_max(1, 17, 33))
#
# # 這裡的 print(find_max)會印出這個功能存放在記憶體的位置
# print(find_max)

# def find_max(num1, num2, num3):
#     if type(num1) != int or type(num2) != int or type(num3) != int:
#         print("請輸入整數")
#         return None
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# max_value = find_max(10, "hu", 7)
# print(max_value)




# below is test 2
# def find_max(num1, num2, num3):
#     if type(num1) != int or type(num2) != int or type(num3) != int:
#         return "請輸入整數"
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# def find_min(num1, num2, num3):
#     if type(num1) != int or type(num2) != int or type(num3) != int:
#         return "請輸入整數"
#     if num1 <= num2 and num1 <= num3:
#         return num1
#     elif num2 <= num1 and num2 <= num3:
#         return num2
#     else:
#         return num3
#
# def max_min(num1, num2, num3):
#     if type(num1) != int or type(num2) != int or type(num3) != int:
#         return "請輸入整數"
#     else:
#         return find_max(num1, num2, num3) - find_min(num1, num2, num3)
#
# # 最後call的是max_min funciton, 其實find_max & find_min可以不用判斷是否為整數。
# num = max_min("77", 11, 3)
# print(num)


# below is project 4

# ===============below is first try=================
# print("歡迎使用綜合健康計算機～\n"
#       "(1) 計算BMI\n"
#       "(2) 計算基礎代謝率（BMR)\n"
#       "(3) 計算總熱量消耗（TDEE）\n")
#
# choose = int(input("請輸入要計算的項目（輸入：1/2/3）"))
#
# def bmi(height, weight):
#     height = float(input("請輸入您的身高（公分）")) / 100
#     weight = float(input("請輸入您的體重（公斤）"))
#     bmi = round(weight / height ** 2, 1)
#     judge = ""
#     if bmi <= 18.5:
#         judge = "體重過輕"
#     elif bmi < 24:
#         judge = "正常體位"
#     elif bmi < 27:
#         judge = "體重過重，重一點而已，還好"
#     elif bmi < 30:
#         judge = "輕度肥胖，已是肥了"
#     elif bmi < 35:
#         judge = "中度肥胖，唉"
#     elif bmi >= 35 :
#         judge = "你已胖到不行"
#     else:
#         print("請輸入指定內容")
#         return
#
#     print(f"您的BMI是：{bmi} ({judge})")
#
#
# def bmr(gender, height, weight, age):
#     gender = input("請輸入您的性別（男/女）").upper()
#     height = float(input("請輸入您的身高（公分）"))
#     weight = float(input("請輸入您的體重（公斤）"))
#     age = int(input("請輸入您的年齡（歲）"))
#     bmr_num = 0
#     if gender == "男" or gender == "M" or gender == "MALE":
#         bmr_num = 66 + (weight * 13.7 + height * 5 - age * 6.8)
#         return bmr_num
#     elif gender == "女" or gender == "F" or gender == "FEMALE" :
#         bmr_num = 655 + (weight * 9.6 + height * 1.8 - age * 4.7)
#         return bmr_num
#     else:
#         print("請重新輸入指定內容")
#
# def tdee(bmr_num, times):
#     bmr_num = bmr("", 0, 0, 0)
#     print("(1)久坐、幾乎沒運動 \n"
#           "(2)每週低強度運動１－３天 \n"
#           "(3)每天中強度運動３－５天 \n"
#           "(4)每天高強度運動６－７天 \n"
#           "(5)勞力密集工作或是每天高強度訓練")
#     times = int(input("請選擇您的運動量（輸入１－５）"))
#     tdee_num = 0
#     if times == 1:
#         tdee_num = bmr_num * 1.2
#     elif times == 2:
#         tdee_num = bmr_num * 1.375
#     elif times == 3:
#         tdee_num = bmr_num * 1.55
#     elif times == 4:
#         tdee_num = bmr_num * 1.725
#     elif times == 5:
#         tdee_num = bmr_num * 1.9
#     else:
#         print("請輸入指定內容")
#         return
#
#
#     return tdee_num
#
#
# if choose == 1:
#     bmi(0,0)
# elif choose == 2:
#     bmr_num = round(bmr("", 0, 0, 0), 2)
#     print(f"您的BMR是：{bmr_num}卡路里")
# elif choose == 3:
#     tdee_num1 = round(tdee(0,0), 2)
#     print (f"您的TDEE是：{tdee_num1}卡路里")
# else:
#     print("錯誤！請輸入您要計算的數值")

#===================above is first try, below is second try==================

# def bmi(height, weight):
#     height /= 100
#     bmi_num = round(weight / height ** 2, 1)
#     return bmi_num
#
# def bmr(gender, height, weight, age):
#     bmr_num = 0
#     if gender == "男" or gender == "M" or gender == "MALE":
#         bmr_num = 66 + (weight * 13.7 + height * 5 - age * 6.8)
#     elif gender == "女" or gender == "F" or gender == "FEMALE" :
#         bmr_num = 655 + (weight * 9.6 + height * 1.8 - age * 4.7)
#     else:
#         print("請重新輸入指定內容")
#     return bmr_num
#
# def tdee(bmr_num, times):
#     tdee_num = 0
#     if times == 1:
#         tdee_num = bmr_num * 1.2
#     elif times == 2:
#         tdee_num = bmr_num * 1.375
#     elif times == 3:
#         tdee_num = bmr_num * 1.55
#     elif times == 4:
#         tdee_num = bmr_num * 1.725
#     elif times == 5:
#         tdee_num = bmr_num * 1.9
#     else:
#         print("請輸入指定內容")
#         return
#
#     return tdee_num
#
#
# print("歡迎使用綜合健康計算機～\n"
#       "(1) 計算BMI\n"
#       "(2) 計算基礎代謝率（BMR)\n"
#       "(3) 計算總熱量消耗（TDEE）\n")
#
# choose = int(input("請輸入要計算的項目（輸入：1/2/3）"))
#
# if choose == 1:
#     height_num = float(input("請輸入身高"))
#     weight_num = float(input("請輸入體重"))
#     bmi_num = round(bmi(height_num,weight_num), 1)
#     print(f"您的BMI是：{bmi_num}")
#
# elif choose == 2:
#     gender_num = input("請輸入性別").upper()
#     height_num = float(input("請輸入身高"))
#     weight_num = float(input("請輸入體重"))
#     age_num = int(input("請輸入年齡"))
#     bmr_num = round(bmr(gender_num, height_num, weight_num, age_num), 2)
#     print(f"您的BMR是：{bmr_num}卡路里")
#
# elif choose == 3:
#     gender_num = input("請輸入性別").upper()
#     height_num = float(input("請輸入身高"))
#     weight_num = float(input("請輸入體重"))
#     age_num = int(input("請輸入年齡"))
#     bmr_num = round(bmr(gender_num, height_num, weight_num, age_num), 2)
#     times_num = int(input("(1)久坐、幾乎沒運動 \n"
#           "(2)每週低強度運動１－３天 \n"
#           "(3)每天中強度運動３－５天 \n"
#           "(4)每天高強度運動６－７天 \n"
#           "(5)勞力密集工作或是每天高強度訓練\n"
#           "請選擇您的運動量（輸入１－５）"))
#     tdee_num1 = round(tdee(bmr_num,times_num), 2)
#     print (f"您的TDEE是：{tdee_num1}卡路里")
# else:
#     print("錯誤！請輸入您要計算的數值")


#==============above is second try, below is solution from teacher============

def get_bmi(height, weight):
    height /= 100
    bmi = weight / height ** 2
    bmi = round(bmi, 2)
    return bmi

def get_bmr(gender, height, weight, age):
    if gender == "男" or gender == "M" or gender == "MALE":
        bmr = 66 + (weight * 13.7 + height * 5 - age * 6.8)
    elif gender == "女" or gender == "F" or gender == "FEMALE":
        bmr = 655 + (weight * 9.6 + height * 1.8 - age * 4.7)
    bmr = round(bmr, 2)
    return bmr

def get_tdee(gender, height, weight, age, times):
    bmr = get_bmr(gender, height, weight, age)
    tdee = bmr * times
    tdee = round(tdee, 2)
    return tdee

# print("歡迎使用綜合健康計算機～\n"
#       "(1) 計算BMI\n"
#       "(2) 計算基礎代謝率（BMR)\n"
#       "(3) 計算總熱量消耗（TDEE）\n")
# choose = int(input("請輸入要計算的項目（輸入：1/2/3）"))
#
# if choose == 1:
#     height = float(input("請輸入身高(cm):"))
#     weight = float(input("請輸入體重(kg)"))
#     bmi = get_bmi(height, weight)
#     print(f"您的BMI是:{bmi}")
# elif choose == 2:
#     gender = input("請輸入您的性別").upper()
#     height = float(input("請輸入身高(cm):"))
#     weight = float(input("請輸入體重(kg)"))
#     age = int(input("請輸入您的年齡"))
#     bmr = get_bmr(gender, height, weight, age)
#     print(f"您的基礎代謝率(BMR)是：{bmr}")
# elif choose == 3:
#     gender = input("請輸入您的性別").upper()
#     height = float(input("請輸入身高(cm):"))
#     weight = float(input("請輸入體重(kg)"))
#     age = int(input("請輸入您的年齡"))
#     print ("(1)久坐、幾乎沒運動\n"
#            "(2)每週低強度運動１－３天\n"
#            "(3)每天中強度運動３－５天\n"
#            "(4)每天高強度運動６－７天\n"
#            "(5)勞力密集工作或是每天高強度訓練")
#     exer = int(input("請選擇您的運動量（輸入１－５)"))
#     times = 0
#     if exer == 1:
#         times = 1.2
#     elif exer == 2:
#         times = 1.375
#     elif exer == 3:
#         times = 1.55
#     elif exer == 4:
#         times = 1.725
#     else:
#         time = 1.9
#     tdee = get_tdee(gender, height, weight, age, times)
#     print(f"您的綜合代謝率(TDEE)是：{tdee}")
#
#
test = "Hello Hi Hi"