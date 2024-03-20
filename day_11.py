# # 模組引入的方法 可以用 as 改掉模組名稱
# import day_10 as q
# q.Question()
#
# # 只想要import某個功能時 可用 from...import...
# from day_10 import Question, QuestionGame
# Question()
# QuestionGame()
#
# # 想使用模組所有功能，又不想每次都先 "day_10.xxx" 的話，from ... import * = import所有功能！
# # 若一次引入許多模組，每個都是import *, 會不知道功能是從哪裡引用來的！
# from day_10 import *
# Question()
# QuestionGame

#============================================================
# package 套件 -> 就是一個可以存放許多模組的資料夾

# 如果想把很多模組包裝成一個套件
# 1. 先在python創建一個資料夾 eg. my_package
# 2. 把想要的模組拉進資料夾 eg. question, question1, question2
# 3. 資料夾內再創建一個新的python檔案，命名必須為 "__init__.py"
# 成功創建一個套件（my_package) 內含三個模組
# import my_package.question
# from my_package import question

# !! 一定要有一個 "__init__.py"的檔案 --> 初始檔案
# 如果只寫 import my_package --> 就會import這個初始檔案

# 套件裡面還可再放套件（一樣要有"__init__"檔案）
# import my_package.sub_package.question3

#============================================================
# tuple 元組
# 與列表的差別：元組一被創建就沒辦法修改！！

# scores = (20, 30, 50, 80, 90)
# print(scores[-1])

#============================================================
# tkinter 套件 可創建GUI圖形介面程式
# 創建視窗、標籤

# from tkinter import *
#
# import tkinter.font as tkFont
#
#
#
# window = Tk() #打開視窗
#
# window.title("第一個圖形程式")
# #設定寬高
# window.geometry("300x300")
# #設定最大寬高
# window.maxsize(width= "400", height= "400")
# #設定最小寬高
# window.minsize(width= "200", height= "200")
# #設定是否能調整寬高
# window.resizable(True, True)
#
# my_label = Label(text="你好嗎", font=("標楷體", 30))
# my_label.pack(side="top")
#
# #tkinter.font.families ==> 電腦裡的所有字體
# print(tkFont.families())
#
# window.mainloop() #關閉視窗

#============================================================
#改變設定、創建按鈕、

# from tkinter import *
#
# window = Tk() #打開視窗
#
# # 設定視窗 .title, .geometry
# window.title("第一個圖形程式")
# window.geometry("300x300")
#
# # 創建標籤 Label
# my_label = Label(text="你好嗎", font=("標楷體", 30))
# my_label.pack(side="top")
#
# # 可以用中括號改變設定
# my_label["text"] = "小黑"
# my_label["font"] = ("Ariel", 20)
# # 也可以用.config來改變設定
# my_label.config(text="你好嗎", font=("Terminal", 25))
#
# def play():
#     print(my_entry.get())
#     Label(text=f"{my_entry.get()}! Ouch!🐥", font=("Terminal", 25)).pack(side="bottom")
#
#
# #創建按鈕 Button
# my_button = Button(text="點我", font=10, command=play) #不知為何font大小調整了也不會跟著變
# my_button.pack(side="top")
#
# #創建輸入框 Entry
# my_entry = Entry(width=10)
# my_entry.pack(side="top")
# #取得輸入框裡的文字
# my_entry.get()
#
# # 數字的輸入框 Spinbox
# def use_spinbox():
#     print(my_spinbox.get())
#
# my_spinbox = Spinbox(from_=0,
#                      to=100,
#                      width=20,
#                      command=use_spinbox)
# my_spinbox.pack()
#
# # 創建拉桿 Scale
# def use_scale(value): #拉桿的值會直接傳回來取代函數，不用再另外get()
#     print(value)
# my_scale = Scale(from_=0, to=100, command=use_scale)
# my_scale.pack()
#
#
# # 創建勾選欄位 Checkbutton
# def use_checkbutton():
#     print(check.get())
# check = IntVar() #這裡就是設定tkinter裡的變數物件 "IntVar()"這個類別, 勾=1, 不勾=0
# my_check = Checkbutton(text="勾我",
#                        variable=check, #變數不可以隨便亂設定，必須是tkinter裡的變數物件
#                        font=0,
#                        command=use_checkbutton)
# my_check.pack()
#
#
# # 創建單選按鈕 Radiobutton
# def use_radiobutton():
#     print(radio.get())
# radio = IntVar()
# my_radio1 = Radiobutton(text="選我～",
#                         value=1,
#                         variable=radio,
#                         font=0,
#                         command=use_radiobutton)
# my_radio2 = Radiobutton(text="選我啦！",
#                         value=2,
#                         variable=radio,
#                         font=0,
#                         command=use_radiobutton)
# my_radio1.pack()
# my_radio2.pack()
#
#
# # 排版/顯示方式 pack, place, grid
#
# # pack(side="top") --> 顯示在上方空間
# # pack(pady=10) --> 設定上下空間 多10像素
# # pack(padx=20) --> 設定左右空間 多20像素
#
# # place(x=150, y=150) --> 直接設定座標 （要看最初設定視窗的像素大小）
# # 座標點會從元件的左上角開始算
# # place(anchor="center", x=200, y=200) --> 可用anchor來設定座標以中心點為主
#
# # grid(row=0, column=0)  --> 以行列來顯示, 是相對顯示！若中間是空的，會自動補上
# # grid(padx=10, pady=10, row=0, column=1) --> 也可用padx/pady來設定間距
#
# # !!注意 grid 與 pack顯示方式 不能混用！！！
#
# # 間距也可在一開始設定視窗時設定
# # window.config(padx=10, pady=10)
#
#
# window.mainloop() #關閉視窗

#=========below is project 11===================================================

def try_float(user_input):
    try:
        user_input = float(user_input)
        return user_input
    except:
        return "請輸入數值"


from tkinter import *

window = Tk()
window.title("BMI計算公式")
window.geometry("550x400")
window.resizable(False, False)
window.config(padx=5, pady=5)

my_label_height = Label(text="身高")
my_label_height.place(anchor="center", x=175, y=137.5)

my_entry_height = Entry(width=10)
my_entry_height.place(anchor="center", x=275, y=137.5)
height = try_float(my_entry_height.get())

my_label_height_end = Label(text="公分")
my_label_height_end.place(anchor="center", x=375, y=137.5)

my_label_weight = Label(text="體重")
my_label_weight.place(anchor="center", x=175, y=170)

my_entry_weight = Entry(width=10)
my_entry_weight.place(anchor="center", x=275, y=170)
weight = try_float(my_entry_weight.get())

my_label_weight_end = Label(text="公斤")
my_label_weight_end.place(anchor="center", x=375, y=170)

my_bmi = Label(text="")
my_bmi.place(anchor="center", x=275, y=215)

def get_bmi():
    height = my_entry_height.get()
    height = float(height) / 100
    weight = my_entry_weight.get()
    weight = float(weight)
    bmi = round(weight / height ** 2, 1)
    if bmi <= 18.5:
        my_bmi["text"] = f"您的BMI為：{bmi}\n 體重過輕 🥹"
    elif bmi < 24:
        my_bmi["text"] = f"您的BMI為：{bmi}\n 正常體位 🥳"
    elif bmi < 27:
        my_bmi["text"] = f"您的BMI為：{bmi}\n 體重稍重，還可以 😄"
    elif bmi < 30:
        my_bmi["text"] = f"您的BMI為：{bmi}\n 輕度肥胖，已是肥了 😄"
    elif bmi < 35:
        my_bmi["text"] = f"您的BMI為：{bmi}\n 中度肥胖 🥹"
    else:
        my_bmi["text"] = f"您的BMI為：{bmi}\n 您已胖到不行 😭"

    return bmi


my_button = Button(text="計算", command=get_bmi)
my_button.place(anchor="center", x=275, y=265)



window.mainloop()


#=======below is solution from teacher===========

# from tkinter import *
#
# window = Tk()
#
# window.title("BMI計算機")
# window.geometry("260x200")
# window.config(padx=50, pady=50)
#
# height_label = Label(text="身高")
# height_label.grid(row=0, column=0)
#
# height_input = Entry(width=10)
# height_input.grid(row=0, column=1)
#
# cm_label = Label(text="公分")
# cm_label.grid(row=0, column=3)
#
#
# weight_label = Label(text="體重")
# weight_label.grid(row=1, column=0)
#
# weight_input = Entry(width=10)
# weight_input.grid(row=1, column=1)
#
# kg_label = Label(text="公斤")
# kg_label.grid(row=1, column=3)
#
# bmi_label = Label(text="您的BMI:0")
# bmi_label.grid(row=2, column=1)
#
# def cal_bmi():
#     height = float(height_input.get())/100
#     weight = float(weight_input.get())
#     bmi = round(weight / height ** 2, 1)
#     bmi_label["text"] = f"您的BMI是:{bmi}"
#
#
# buttom = Button(text="計算", command=cal_bmi)
# buttom.grid(row=3, column=1)
#
# window.mainloop()
