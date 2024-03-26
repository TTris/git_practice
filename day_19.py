# 發送 requests 傳入參數

# import requests as req
# import pandas as pd
#
# params = {
#     "Authorization" : "CWA-01B95BFF-98D9-488C-8FEA-E1157A21162D",
#     "locationName" : "新北市",
#     "elementName" : "PoP"
# }
#
# res = req.get("https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001", params=params)
#
# print(res.json()["records"]["location"][0]["weatherElement"][0]["time"][0]["parameter"]["parameterName"])

#===========================================================================
# 發送mail 可用 import smtplib 或是 import email.message

# import smtplib
# import email.message
#
# my_email = "tristatsai725@gmail.com"
# password = "vqhsumkyegyiiamt"
#
# msg = email.message.EmailMessage()
# msg["From"] = my_email
# msg["To"] = "mctsai725@gmail.com"
# msg["Subject"] = "Python practice 1"
# msg.set_content("first message")
#
# connection = smtplib.SMTP_SSL("smtp.gmail.com")
# connection.login(my_email, password)
# connection.send_message(msg)
# connection.close()


#=================below is test 2==========================================================
# import datetime
# import smtplib
# import email.message
# import schedule
# import time
#
# my_email = "tristatsai725@gmail.com"
# password = "vqhsumkyegyiiamt"
#
# mail_no = 1
#
# def sent_mail():
#     global mail_no
#     current_time = datetime.datetime.now()
#     formatted_time = current_time.strftime("%Y-%m-%d %H-%M-%S")
#
#     msg = email.message.EmailMessage()
#     msg["From"] = my_email
#     msg["To"] = "mctsai725@gmail.com"
#     msg["Subject"] = f"Python practice {mail_no}"
#     msg.set_content(f"來自 {formatted_time} 的python Hello 信")
#
#     connection = smtplib.SMTP_SSL("smtp.gmail.com")
#     connection.login(my_email, password)
#     connection.send_message(msg)
#     connection.close()
#
#     print(f"第{mail_no}封信 {formatted_time} 發送成功")
#     mail_no += 1
#
#
# schedule.every().minute.do(sent_mail)
#
# while True:
#     schedule.run_pending()
#     time.sleep(60)


#=================below is project 19==========================================================

import requests as req
import smtplib
import email.message


params = {
    "Authorization" : "CWA-01B95BFF-98D9-488C-8FEA-E1157A21162D",
    "locationName" : "桃園市",
}

res = req.get("https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001", params=params)
if_rain = int(res.json()["records"]["location"][0]["weatherElement"][1]["time"][0]["parameter"]["parameterName"])
tem = int(res.json()["records"]["location"][0]["weatherElement"][2]["time"][0]["parameter"]["parameterName"])


my_email = "tristatsai725@gmail.com"
password = "vqhsumkyegyiiamt"



msg = email.message.EmailMessage()
msg["From"] = my_email
msg["To"] = "mctsai725@gmail.com"
msg["Subject"] = f"Python practice for weather"

content = ""

if if_rain >= 20:
    content += "開車上班\n"
else:
    content += "騎機車\n"

if tem <= 15:
    content += "穿羽絨"
elif tem <= 20:
    content += "穿長袖＋外套"
elif tem <= 25:
    content += "穿長袖"
else:
    content += "穿短袖"

msg.set_content(content)

connection = smtplib.SMTP_SSL("smtp.gmail.com")
connection.login(my_email, password)
connection.send_message(msg)
connection.close()

print("發送成功")

