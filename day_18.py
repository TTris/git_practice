# API (Applicaiton Programming Interface) -> 其他裝置的函數
# 應用程式介面

# 第三方套件 發送請求到網址 requests
# import requests as req
# res = req.get("https://openapi.twse.com.tw/v1/company/newlisting")
# print(res)
# print(res.text)
# print(res.json())
# print(res.json()[0])
# print(res.json()[0]["Company"])
#
# res = req.get("https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL")
# print(res.json()[:5])

# 回應碼:
# 1XX: informational
# 2XX: Successful
# 3XX: Redirects
# 4XX: Client Errors
# 5XX: Server Errors


# pandas DataFrame, Series

import pandas as pd

# pandas.Series() 創建一維資料

# a = pd.Series([20, 50, 30])
# print(a)

# pandas.DataFrame() 創建二維資料

# b = {
#     "name": ["Red", "Blue", "Yellow", "Pinky"],
#     "age": [32, 18, 14, 26],
#     "gender": ["Female","Male","Female","Male"],
#     "height": [180, 169, 177, 159]
# }
#
# b = pd.DataFrame(b)
# print(b)
#
# print(b["age"].max())


# c = [
#     {"name": "Red", "age": 18, "gender": "Male"},
#     {"name": "Purple", "age": 56, "gender": "Male"},
#     {"name": "Rock", "age": 34, "gender": "Female"},
#     {"name": "Flower", "age": 23, "gender": "Female"},
# ]
#
# c = pd.DataFrame(c)
# print(c)

#=====================below is test 1===================================================

# import requests as req
# import pandas as pd
#
#
# res = req.get("https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL")
# data = pd.DataFrame(res.json())
# data.to_csv("Day 18 test1", encoding="utf_8_sig")


#========================================================================
# 排程 定時執行 特定時間執行
# 第三方套件 schedule
# import schedule
# import time
#
#
# def job1():
#     print("任務一")
#
# def job2(a):
#     print(f"任務二{a}")
#
#
# # by second
# # a = 0
# # schedule.every(2).seconds.do(job1)
# # schedule.every().second.do(job2,a)
#
# # by minute
# schedule.every().minute.do(job1)
# schedule.every().minute.at(":30").do(job2, "Hi")  #每分鐘的30秒執行一次
#
# # by hour
# schedule.every().hour.do(job1)
# schedule.every(2).hours.at(":20:30").do(job1)
#
# # by day
# schedule.every().day.at("08:30:00").do(job1)
#
# # by week
# schedule.every().sunday.at("08:45:15").do(job1)
#
#
# while True:
#     schedule.run_pending()  # 檢查時間來執行
#     time.sleep(1)           # 此函式可讓程式暫停()秒
#================below is project 18========================================================
import schedule
import time
import requests as req
import pandas as pd
import datetime

def get_stock():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H-%M-%S")
    res = req.get("https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL")
    data = pd.DataFrame(res.json())
    data.to_csv(f"{formatted_time} Day 18 Project", encoding="utf_8_sig")
    print(f"{formatted_time} 取得股票資訊")

schedule.every(5).seconds.do(get_stock)

while True:
    schedule.run_pending()
    time.sleep(1)

