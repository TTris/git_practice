# 讀取、寫入  檔案

#打開 ->  open(要打開的檔案, 打開的模式)
#打開 ->  open(要打開的檔案, 打開的模式, encoding="utf-8") 還可以加上第三個參數 編碼
#打開的模式:
# r: 讀數
# w: 複寫
# a: 在原先的資料再寫東西 （新增）
# 開完之後要關閉 .close() !!!
#
# open("123.txt", "r")
# file = open("123.txt", "r")

# print(file.read())
# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)
#
# file.close()
#
# #=====
#
# open("123.txt", "w")
# file_2 = open("123.txt", "w")
# #要寫之前還要先 .write()
# file_2.write("123")
# file_2.write("Hello")
#
# file_2.close()

#====
# open("123.txt", "a", encoding="utf-8")
# file_3 = open("123.txt", "a")
# file_3.write("\n")
# file_3.write("567")
# file_3.write("\n")
# file_3.write("小白")
# file_3.close()
#
# #可用with 跟 as 來執行，就不用再 .close() --> 2個方式是一樣的
# with open("123.txt", "a", encoding="utf-8") as file_4:
#     file_4.write("\n")
#     file_4.write("小白")

#===========================================================

# file = open("123.txt", "r")
#
# num = 0
# for i in range(1, 8):
#     num += int(file.readline())
#
# print(num)

#========below is solution from teacher========
# total = 0
# with open("123.txt", "r") as file:
#     for line in file:
#         total += int(line)
# print(total)

#================================================
# 絕對路徑 vs 相對路徑
# 絕對路徑：從電腦最初的位置開始寫，一路寫到檔案名稱 eg. C:/Users/hibyby/PycharmProjects/begin 1/123.txt
#           對123.txt按著ctrl點選>Open In>Finder>複製路徑，得到以下
#           /Users/tsaimeichih/PycharmProjects/begin 1/123.txt
#           Note 1. 若是windows的話，"\" 要改成 "/"
#           Note 2. 複製路徑後，要再加上檔案名稱，才會是該檔案的絕對路徑 （不然會是它的上一層）
# 相對路徑：根據目前程式的位置做延伸 eg. 123.txt
#         Note 1. 等於程式會在前面自動補上目前程式的所在位置
#         Note 2. 若想回到目前程式所在位置的「上一層」，可寫「../」-> 代表回到上一個資料夾
#                 同理，若想回到目前程式所在位置的「上上一層」，可寫「../../」

# open("123.txt", "r")
#       ^^^^^^^這裡可以寫絕對路徑，也可寫相對路徑
#
# with open("/Users/tsaimeichih/PycharmProjects/begin 1/123.txt", "r") as file:
#     print(file.read())

#==============================================

# json 模組 ->

import json

# password = {
#     "account": "123456789",
#     "password": "123"
# }
#
# with open("123.txt", "w") as file:
#     # import json後 json.dumps 可將資料存成json字串
#     # 若想資料縮排，可加入第二個參數 indent=
#     file.write(json.dumps(password, indent= 4))

# with open("123.txt", "r") as file:
#     # import json後 json.loads可將json字串傳回python格式的資料
#     # 這樣就可以正常取值
#     x = json.loads(file.read())
#     print(x["account"])




# password = [1, 2, 3, 4, 5]
#
# with open("123.txt", "w") as file:
#     # import json後 json.dumps 可將資料存成json字串
#     # 若想資料縮排，可加入第二個參數 indent=
#     file.write(json.dumps(password))
#
# with open("123.txt", "r") as file:
#     # import json後 json.loads可將json字串傳回python格式的資料
#     # 這樣就可以正常取值
#     x = json.loads(file.read())
#     print(x[3])

# 補充１：通常儲存json格式的檔案，我們會取為xxx.json
# 補充２：若目前想寫入的文件在檔案夾裡找不到，python會一你命名自動創建


#=======below is projet 9======================
#
# print("歡迎您使用密碼管理器")
# user_funtion = input("請問要使用什麼功能呢？\n"
#                 "輸入「R」為查詢； 「A」為新增； 「Q」為離開\n").upper()
#
# user_input = {
#
# }
#
# while user_funtion != "Q":
#     if user_funtion == "A":
#         user_platform = input("請輸入帳號名稱：")
#         user_account = input("請輸入帳號：")
#         user_password = input("請輸入密碼：")
#         with open("user_password.json", "r") as file:
#             file = json.loads(file.read())
#             if user_platform in user_input:
#                 print("已有此筆資料\n")
#             else:
#                 with open("user_password.json", "w") as file:
#                     user_input[user_platform] = {"account": user_account, "password": user_password}
#                     file.write(json.dumps(user_input, indent= 4))
#                     print("新增成功\n")
#
#     elif user_funtion == "R":
#         user_search = input("請輸入要查詢的帳號：")
#         with open("user_password.json", "r") as file:
#             file = json.loads(file.read())
#             try:
#                 print(f"您的帳號是：{file[user_search]["account"]}、密碼是：{file[user_search]["password"]}\n")
#             except:
#                 print("查無此資料，請重新確認")
#     else:
#         print("請確認您要使用的功能\n")
#
#     user_funtion = input("請問要使用什麼功能呢？\n"
#                              "輸入「R」為查詢； 「A」為新增； 「Q」為離開\n").upper()
#
# print("感謝使用")


#=============below is solution from teacher

import json

def get_password_dic():
    with open("password.json", "r") as f:
        password_str = f.read()
        if password_str == "":
            return {}
        else:
            return json.loads(password_str)

def check_name(name):
    password_dic = get_password_dic()
    if name in password_dic.keys():
        return False
    else:
        return True

def add_password(name, account, password):
    if check_name(name):
        password_dic = get_password_dic()
        password_dic[name] = {
            "account": account,
            "password": password
        }
        with open("password.json", "w") as f:
            f.write(json.dumps(password_dic))
        return True
    else:
        return False


print("歡迎您使用密碼管理器")

while True:
    mode = input("請問要使用什麼功能呢？\n"
                    "輸入「R」為查詢； 「A」為新增； 「Q」為離開\n").upper()
    if mode == "Q":
        print("感謝使用")
        break
    elif mode == "A":
        name = input("請輸入帳號名稱：")
        account = input("請輸入帳號：")
        password = input("請輸入密碼：")
        if add_password(name, account, password):
            print("新增成功\n")
        else:
            print("已有此帳號名稱\n")
    elif mode == "R":
        name = input("請輸入想查詢的帳號名稱：")
        if check_name(name):
            print("查無此帳號\n")
        else:
            password_dic = get_password_dic()
            account = password_dic[name]["account"]
            password = password_dic[name]["password"]
            print(f"帳號：{account}, 密碼：{password}")