# 資料型態 dictionary：
# 鍵       值   的配對
# key    value
# "蘋果" "apple"
# "香蕉" "banana"
#
# eng_dic = {
#     "蘋果" : "apple",
#     "香蕉":"banana",
#     "貓" : "cat",
#     "age": 23,
#     "score": 60.5,
#     "is_male": True
# }
#
# print(eng_dic["is_male"])
# eng_dic["is_male"] = "haha"
#
# print(eng_dic["蘋果"])
# print(eng_dic["is_male"])
#
# eng_dic["你好"] = 5.8
# print(eng_dic)
#
# for key in eng_dic:
#     print(key)  #印出來的是key
#     print(eng_dic[key])  #把value取出來，印出value


#=========below is test 1============

# customer_spending = {
# 	"小白": 2000,
#     "小黑": 3000,
#     "小黃": 12000,
#     "小綠": 15000,
#     "小灰": 8000
# }
#
# for key in customer_spending:
#     if customer_spending[key] >= 10000:
#         customer_spending[key] = "VIP"
#     else:
#         customer_spending[key] = "一般客戶"
#
#
# print(customer_spending)


#=====below is more application for dictionary==========

# students = {
#     "name": ["小白", "小黑", "小綠"],
#     "age":{
#         "小白" : 23,
#         "小黑" : 15,
#         "小綠" : 20
#     }
# }
#
# students["name"][1]
# print(students["name"][1])
#
# students["age"]["小黑"]
# print(students["age"]["小黑"])
#
#
# students_list = [
#     {
#         "name" : "小白",
#         "age" : 23,
#
#     },
#     {
#         "name" : "小黑",
#         "age" : 15
#     },
#     {
#         "name" : "小藍",
#         "age" : 18
#     }
# ]
#
# students_list[2]["name"]
# print(students_list[2]["name"])
#
#
# #列表常搭配的函數
# #.keys() -> 取得key, 只顯示，不能取值   // 可搭配list變回字串後取值
#
# print(eng_dic.keys())
#
# print(students.keys())
# print(list(students.keys())[0])
# print(list(eng_dic))   #直接用list也會取出key
#
# #.values() -> 取得values,
# print(eng_dic.values())
# print(list(eng_dic.values())[2])

#===========below is test 2==============
# import random
#
# students = {
#     "小白": {
#         "age": 23,
#         "height": 170.5,
#         "weight": 60
#     },
#     "小黃": {
#         "age": 30,
#         "height": 160.5,
#         "weight": 38
#     },
#     "小綠": {
#         "age": 15,
#         "height": 160.5,
#         "weight": 38}
#     }
#
# print("抽到的是:", end='')
#
# if "".join(random.sample(list(students),1)) == "小白":
#     print("小白")
#     print("年紀:", end="")
#     print(students["小白"]["age"])
#     print("身高:", end="")
#     print(students["小白"]["height"])
#     print("體重:", end="")
#     print(students["小白"]["weight"])
# elif "".join(random.sample(list(students),1)) == "小黃":
#     print("小黃")
#     print("年紀:", end="")
#     print(students["小黃"]["age"])
#     print("身高:", end="")
#     print(students["小黃"]["height"])
#     print("體重:", end="")
#     print(students["小黃"]["weight"]),
# else:
#     print("小綠")
#     print("年紀:", end="")
#     print(students["小綠"]["age"])
#     print("身高:", end="")
#     print(students["小綠"]["height"])
#     print("體重:", end="")
#     print(students["小綠"]["weight"])
#
# print()
#
#
# #=====solution from teacher===========
# students_name = list(students)
# random_name = students_name[random.randint(0, 2)]
# print(f"抽到的是{random_name}")
# print(f"年紀：{students[random_name]["age"]}")
# print(f"身高：{students[random_name]["height"]}")
# print(f"體重：{students[random_name]["weight"]}")




#==========below is project 7============
import random

eng_dic = {
    "蘋果": "apple",
    "香蕉": "banana",
    "貓": "cat",
    "狗": "dog",
    "蛋": "egg",
    "食物": "food",
    "遊戲": "game",
    "手": "hand",
    "冰": "ice",
    "果醬": "jam",
    "國王": "king",
    "標籤": "label",
    "郵件": "mail",
    "脖子": "neck",
    "油": "oil",
    "豬": "pig",
    "皇后": "queen"
}

# num_practice = int(input("請問要練習幾題？"))
# i = 0
# correct = 0
# wrong = 0
#
# question = list(eng_dic)[random.randint(0, len(list(eng_dic)))]
#
# while i < num_practice:
#     answer = input(f"請問「{question}」的英文是：")
#     if answer == eng_dic[question]:
#         print("你答對了！")
#         correct += 1
#     else:
#         print(f"你答錯了，答案是：{eng_dic[question]}")
#         wrong += 1
#     question = list(eng_dic)[random.randint(0, len(list(eng_dic))-1)]
#
#     i += 1
#
# print(f"總共{num_practice}題，答對了{correct}題，答錯了{wrong}題")


#========below is solution from teacher==========
question_num = int(input("請問你想練習幾題？"))
questions = list(eng_dic)
score = 0

for i in range (1, question_num + 1):
    random_question = questions[random.randint(0, len(questions) + 1)]
    print(f"第{i}題：")
    ans = input(f"請問「{random_question}」的英文是：")
    if ans == eng_dic[random_question]:
        print("你答對了！")
        score += 1
    else:
        print(f"你答錯了，答案是：{eng_dic[random_question]}")

print(f"總共{question_num}題，答對了{score}題，答錯了{question_num-score}題")