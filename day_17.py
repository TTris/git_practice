# [] 取值、創建列表字典 進階用法
#
# #取值
# score = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# print(score[0:3])  # 從０取到３但不包含第三位
# print(score[5:-1])
# print(score[5:])   # 冒號後不寫，代表取到最後一位
# print(score[:5])   # 冒號前不寫，代表從第一位開始取
#
# a = "123456789"
# print(a[:3])
#
#
# #創建列表的進階用法:
# #原本寫法
# new_score = []
# for i in score:
#     new_score.append(i+10)
#
# print(new_score)
#
# # 進階寫法
# new_score = [i+10 for i in score]
# print(new_score)
# new_score = [i for i in range(1,5)]  # in "range", not in score
# print(new_score)
# new_score = [i*3 for i in range(1,5)]
# print(new_score)
#
# new_score = [i*2 for i in score if i>60]  #後面可以再加判斷
# print(new_score)
#
#
# #創建字典的進階用法
#
# score_dic = {
#     "分數一": 60,
#     "分數二": 70,
#     "分數三": 80
# }
#
# print(score_dic.items()) #回傳key and value 用元組表示
# for i in score_dic.items():
#     print(i)
#
# for key, value in score_dic.items(): #可用２個變數分別表示 key / value
#     print(key)
#     print(value)
#
# new_score_dic = {key:value+10 for key, value in score_dic.items()}
# print(new_score_dic)
#
# new_score_dic = {"考試"+key:value for key, value in score_dic.items() if value > 60}
# print(new_score_dic)
import pandas as pd

#======================below is test 1==================================================

# score = {
#     "一班小白": 60,
#     "二班小黑": 70,
#     "一班小蘭": 80,
#     "三班小輝": 50,
#     "一班小局": 10,
#     "一班小黃": 20,
#     "二班小綠": 80,
#     "一班小洪": 40
# }
#
# new_score = {key[2:]:value+10 for key, value in score.items() if key[0]=="一"}
# print(new_score)

#========================================================================
# 數據分析套件pandas
#
# #原先寫法
# with open("data.csv", "r", encoding="utf-8") as f:
#     sum = 0
#     for line in f:
#         if line[5] != "別":
#             sum += int(line[5:7])
#     print(sum)
#
# #使用pandas寫法
# import pandas
# data = pd.read_csv("data.csv")  # 用 pd.read 來讀取
# print(data)
#
# # 取得列
# print(data["年紀"])
# print(data["年紀"].sum())
# print(data["年紀"].max())
# print(data["年紀"].min())
# print(data["年紀"].mean())   # 計算平均
# print(data[["身高","年紀"]])  # 可以取多列
#
# # 取得行
# print(data[0:3])
# print(data[2:-1])
# print(data[:5])
#
# # 混用
# print(data[["姓名","身高"]][0:3])
# print(data[4:][["姓名","年紀"]])
#========================================================================


