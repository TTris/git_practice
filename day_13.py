# tkinter messagebox 產生訊息框

# from tkinter import messagebox
# from tkinter import *
# from PIL import ImageTk
#
# # messagebox.showinfo(title="123", message="Hi")
#
# # messagebox.showerror(title="123", message="Error")
#
# # messagebox.showwarning(title="123", message="Warning")
#
# # messagebox.askyesno(title="123", message="choose")  #按下yes回傳True，按下no回傳False
#
# # messagebox.askokcancel(title="123", message="proceed?")  #按下ok回傳True，按下cancel回傳False
#
# window = Tk()
# window.config(padx=100, pady=100)
# window.title("Hello! How are you today?")
#
# def show_message():
#     a = messagebox.askyesno(title="123", message="Are you ok?")
#     return a
#
# def say_hi():
#     if show_message():
#         hi_label["text"] = "I'm happy when you're happy 😍"
#     else:
#         hi_label["text"] = "It's gonna be ok 🥹"
#
#
# b = Button(text="👉🏻press me👈🏻", command=say_hi)
# b.pack()
#
# hi_label = Label(text="")
# hi_label.pack()
#
#
#
# window.mainloop()


# ===================below is test 1===========================================


# import json
# from tkinter import *
# from PIL import ImageTk
# from tkinter import messagebox
#
# window = Tk()
# window.config(padx=20, pady=20)
# window.title("密碼管理器")
#
#
# def get_password_dic():
#     with open("password.json", "r") as f:
#         password_str = f.read()
#         if password_str == "":
#             return {}
#         else:
#             return json.loads(password_str)
#
# def check_name(name):
#     password_dic = get_password_dic()
#     if name in password_dic.keys():
#         return False
#     else:
#         return True
#
# def add_password(name, account, password):
#     if check_name(name):
#         password_dic = get_password_dic()
#         password_dic[name] = {
#             "account": account,
#             "password": password
#         }
#         with open("password.json", "w") as f:
#             f.write(json.dumps(password_dic))
#         return True
#     else:
#         return False
#
# def enter_dic():
#     name = entry_account_name.get()
#     account = entry_account.get()
#     password = entry_password.get()
#     result = add_password(name, account, password)
#     if name == "" or account == "" or password == "":
#         messagebox.showerror(title="新增失敗", message="輸入框不可為空")
#         return False
#     elif result == False:
#         messagebox.showerror(title="新增失敗", message="已有此帳號")
#         return False
#     elif name != "" and account != "" and password != "":
#         messagebox.showinfo(title="新增成功", message="新增成功")
#
#         # 輸入框清除
#         entry_account_name.delete(0, 'end')
#         entry_account.delete(0, 'end')
#         entry_password.delete(0,'end')
#
#         return True
#
#
#
#
#
# img = ImageTk.PhotoImage(file="lock.png")
# canvas = Canvas(width=225, height=225, highlightthickness=0)
# canvas.create_image(112.5, 112.5, image=img)
# canvas.grid(row=0, column=0, columnspan=2)
#
# label_account_name = Label(text="帳號名稱")
# label_account_name.grid(row=1, column=0)
#
#
# entry_account_name = Entry(width=20)
# entry_account_name.grid(row=1, column=1)
#
#
# label_account = Label(text="帳號")
# label_account.grid(row=2, column=0)
#
# entry_account = Entry(width=20)
# entry_account.grid(row=2, column=1)
#
#
# label_password = Label(text="密碼")
# label_password.grid(row=3, column=0)
#
# entry_password = Entry(width=20)
# entry_password.grid(row=3, column=1)
#
#
#
# buttom = Button(text="新增", width=10, bg="#0066CC",command=enter_dic)
# buttom.grid(row=4, column=0, columnspan=2)
#
#
# window.mainloop()


# ==============================================================
# 錯誤處理 try... except... else
#
# try:
#     age = int(input("請輸入年紀: "))
#     print(f"你的年紀是: {age}")
#
# except ValueError as err:       # except後面可以 指定 哪種錯誤類型 才執行下面程式碼
#     print("輸入有誤")            # 可以 as __變數__ ， 此變數會印出錯誤種類
#     print(err)
# except IndexError:              # 想知道有哪些錯誤類型，可google "python exception documentation"
#     print("錯的是index")
# else:
#     print("Heyyy It's else")         # 沒有發生錯誤，會執行此行程式碼
# finally:
#     print("Bye.")               # 不管上面有沒有錯誤，都會印出finally內的程式碼


# ==============================================================
# 發起錯誤

# age = input("請輸入你的年紀：")
# age = int(age)
#
# if age < 0:
#     raise ValueError("年紀不可為負數")

# ========================below is test 2======================================


#
# def try_float(user_input):
#     try:
#         user_input = float(user_input)
#         return user_input
#     except:
#         return "請輸入數值"
#
#
# from tkinter import *
# from tkinter import messagebox
#
# window = Tk()
# window.title("BMI計算公式")
# window.geometry("200x150")
# window.config(padx=15, pady=15)
#
# my_label_height = Label(text="身高")
# my_label_height.grid(row=0, column=0)
#
# my_entry_height = Entry(width=10)
# my_entry_height.grid(row=0, column=1)
# height = try_float(my_entry_height.get())
#
# my_label_height_end = Label(text="公分")
# my_label_height_end.grid(row=0, column=2)
#
# my_label_weight = Label(text="體重")
# my_label_weight.grid(row=1, column=0)
#
# my_entry_weight = Entry(width=10)
# my_entry_weight.grid(row=1, column=1)
# weight = try_float(my_entry_weight.get())
#
# my_label_weight_end = Label(text="公斤")
# my_label_weight_end.grid(row=1, column=2)
#
# my_bmi = Label(text="")
# my_bmi.grid(row=2, column=0, columnspan=3)
#
# def get_bmi():
#     try:
#         height = my_entry_height.get()
#         height = float(height) / 100
#         weight = my_entry_weight.get()
#         weight = float(weight)
#         bmi = round(weight / height ** 2, 1)
#         if height < 0 or weight < 0:
#             raise ValueError("weight and height cannot be negatives")
#     except:
#         messagebox.showerror(title="輸入錯誤", message="亂輸入哦 👎🏼")
#     else:
#         if bmi <= 18.5:
#             my_bmi["text"] = f"您的BMI為：{bmi}\n 體重過輕 🥹"
#         elif bmi < 24:
#             my_bmi["text"] = f"您的BMI為：{bmi}\n 正常體位 🥳"
#         elif bmi < 27:
#             my_bmi["text"] = f"您的BMI為：{bmi}\n 體重稍重，還可以 😄"
#         elif bmi < 30:
#             my_bmi["text"] = f"您的BMI為：{bmi}\n 輕度肥胖，已是肥了 😄"
#         elif bmi < 35:
#             my_bmi["text"] = f"您的BMI為：{bmi}\n 中度肥胖 🥹"
#         else:
#             my_bmi["text"] = f"您的BMI為：{bmi}\n 您已胖到不行 😭"
#
#         return bmi
#
# my_button = Button(text="計算", command=get_bmi)
# my_button.grid(row=3, column=0, columnspan=3)
#
#
#
# window.mainloop()

# ====================below is project 13==========================================


import json
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

window = Tk()
window.config(padx=20, pady=20)
window.title("密碼管理器")


def get_password_dic():
    try:
        with open("password.json", "r") as f:
            password_str = f.read()
            if password_str == "":
                return {}
            else:
                return json.loads(password_str)
    except:
        with open("password.json", "w") as f:
            password_str = f.write()
            if password_str == "":
                return {}


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


def enter_dic():
    name = entry_account_name.get()
    account = entry_account.get()
    password = entry_password.get()
    if name == "" or account == "" or password == "":
        messagebox.showerror(title="新增失敗", message="輸入框不可為空")
        return False
    elif not check_name(name):
        messagebox.showerror(title="新增失敗", message="已有此帳號")
        return False
    else:
        add_password(name, account, password)
        messagebox.showinfo(title="新增成功", message="新增成功")

        # 輸入框清除
        entry_account_name.delete(0, 'end')
        entry_account.delete(0, 'end')
        entry_password.delete(0, 'end')

        return True


def look_for():
    try:
        password_dic = get_password_dic()
        name = entry_account_name.get()
        account = password_dic[name]["account"]
        password = password_dic[name]["password"]
        messagebox.showinfo(title=f"查詢{name}帳號", message=f"帳號：{account}\n 密碼：{password}")
    except:
        get_password_dic()
        messagebox.showerror(title="查詢失敗", message="查無此帳號")


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

buttom_find = Button(text="搜尋", width=10, bg="#8E8E8E", command=look_for)
buttom_find.grid(row=4, column=0, columnspan=2)

buttom = Button(text="新增", width=10, bg="#0066CC", command=enter_dic)
buttom.grid(row=5, column=0, columnspan=2)

window.mainloop()
