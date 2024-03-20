# 函數的進階用法
# 函數參數預測值

# def fun(a, b, c=3):    #這樣寫 c=3 是在幫c設定預設值，後續呼叫函數若無寫上c值，會代入預設值，而不會顯示error: require argument
#     print(a, b, c)
#
# fun(1, 2)
# fun(1, 2,5)

#======================
# 函數進階用法
# *args 傳入多個參數（幾個都可以）

# def add(*nums):  #在前面 +星號 * 代表傳入多個值，並用元組來表示
#     total = 0
#     for num in nums:
#         total += num
#     return total
#
# print(add(1, 2, 3))
#
#
# def add(a, *nums):  #在前面 +星號 * 代表傳入多個值，並用元組來表示
#     print(a)
#     print(nums)
#
# add(1,2,3,4,5)



#======================
# 函數進階用法
# **kwargs 傳入多個指定參數（幾個都可以）

# def add(**nums):  #在前面 +2個星號 ** 代表傳入多個指定參數，並用字典來表示
#     for num in nums:
#         print(num)
#         print(nums[num])
#
# add(num1=1, num2=2, num3=3)

# def add(**nums):  #在前面 +2個星號 ** 代表傳入多個指定參數，並用字典來表示
#     total = 0
#     for num in nums:
#         total += nums[num]
#     return total
#
# print(add(num1=1, num2=2, num3=3))

# def add(a, **nums):  #在前面 +2個星號 ** 代表傳入多個指定參數，並用字典來表示
#     print(a)
#     print(nums)
#
# add(13, num1=1, num2=2)



#======================
# 安裝第三方套件 （使用別人寫好的程式碼）
# search "pypi"
# google "python第三方__想使用的目的__"  > 看大家推薦的 > 複製名稱到 pypi貼上
# 左上角會有 "pip install xxxx" 的複製連結 > copy > 到python 左邊功能選單找terminal > paste > 等他跑完
# 安裝的東西會在 External Libraries > site-packages 裡面

# 解除安裝:
# 安裝時的指令 "pip install xxxxx" 。 則輸入 "pip uninstall xxxxx" 為解除安裝的指令


# 安裝方法2:
# 點選左上角PyCharm > Settings > Project xxx >  Python interpreter > 點選「+」 搜尋想要的第三方套件 > install package

# 解除安裝方法2:
# 同路徑 > 點選「-」即解除安裝

#====================================================
# tkinter 設定顏色 加入圖片（第三方套件pillow)

# from tkinter import *
#
# window = Tk()
# window.config(padx=50, pady=50, bg="#FFCBB3")
#
# # label = Label(text="Hello!", font=20, bg="black", fg="#E2C2DE")  # 用bg=來設定文字標籤的背景顏色 (background)
# # label.pack()                                                  # 除了寫顏色的英文，也可搜尋色碼表 放上顏色的編碼
# #
# # button = Button(text="press me!", font=2, fg="pink") # 用fg=來設定文字本身的顏色 (foreground)
# # button.pack()
#
#
# from PIL import ImageTk  #實際使用 pillow 要寫 import PIL, 因為該模組的資料夾名稱為 PIL
#
# # 用 ImageTk 裡的 PhotoImage來載入圖片， “” 中寫上路徑
# img = ImageTk.PhotoImage(file="meow.png")
# # 此為設定視窗縮圖的程式碼 (windows會在左上角  mac會在dock裡)
# window.iconphoto(True, img)  # True代表「新增的視窗」左上角的圖示是否為該圖示
# # 新視窗可用toplevel
# Toplevel()
#
# # 要創建畫布，把圖片放上去，用Canvas
# canvas = Canvas(width=459, height=328, bg="pink", highlightthickness=0) #highlightthickness是畫布的邊框
# # 用create_image() 畫上去。要設定三個參數：1&2 圖片中心點在畫布的位置, 3.要載入的圖片image=
# canvas.create_image(229.5, 164, image=img)
# canvas.pack()
#
# window.mainloop()

#===========================================================================
# grid 格子顯示 佔用多格

# from tkinter import *
#
# window = Tk()
# window.config(padx=100, pady=100)
#
# label1 = Label(bg="red", width=20, height=5)
# label1.grid(row=0, column=0)
#
# label2 = Label(bg="yellow", width=20, height=5)
# label2.grid(row=1, column=1)
#
# label3 = Label(bg="blue", width=40, height=5)   # 若不將 width變寬，會變成置中
# label3.grid(row=2, column=0, columnspan=2)      # 使用 columnspan 讓顏色佔多格
#
# window.mainloop()


#==================below is project 12==========================

import json
from tkinter import *
from PIL import ImageTk

window = Tk()
window.config(padx=20, pady=20)


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




img = ImageTk.PhotoImage(file="lock.png")
canvas = Canvas(width=225, height=225, highlightthickness=0)
canvas.create_image(112.5, 112.5, image=img)
canvas.grid(row=0, column=0, columnspan=2)

label_account_name = Label(text="帳號名稱")
label_account_name.grid(row=1, column=0)


entry_account_name = Entry(width=20)
entry_account_name.grid(row=1, column=1)


label_account = Label(text="帳號")
label_account.grid(row=2, column=0)

entry_account = Entry(width=20)
entry_account.grid(row=2, column=1)


label_password = Label(text="密碼")
label_password.grid(row=3, column=0)

entry_password = Entry(width=20)
entry_password.grid(row=3, column=1)

label_success = Label(text="")
label_success.grid(row=5, column=0, columnspan=2)

def enter_dic():
    name = entry_account_name.get()
    account = entry_account.get()
    password = entry_password.get()
    add_password(name, account, password)
    if name != "" and account != "" and password != "":
        label_success["text"] = "新增成功"
    return True

buttom = Button(text="新增", width=10, bg="#0066CC",command=enter_dic)
buttom.grid(row=4, column=0, columnspan=2)


window.mainloop()

