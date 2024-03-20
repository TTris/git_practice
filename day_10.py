# 類別class, 物件object, 屬性attibute

# class Phone:      #通常資料型態 取名原則 第一個字為大寫
#         pass      #設定class時，不能為空白。至少要寫上「pass」-> 表示現在未定

# 根據class所創建的東西，就是物件object
# below "phone1" & "phone2" 都是 Phone這個class的物件(object)

#這樣寫就會創建出手機的資料
# phone1 = Phone()
# phone1.number = "213456789" # 這樣寫就是幫phone1創建一個number的屬性. 想要創建幾個屬性都可以
# phone1.price = 8000
# phone1.waterproof = True
# print(phone1.number)
# print(phone1.price)
# print(phone1.waterproof)
#
# phone2 = Phone()
# phone2.number = "AA124"
# phone2.price = 87878
# print(phone2.number)
# print(phone2.price)



# 補充pass可用於迴圈、定義
# def aa():
#         pass
# aa()

#=======================================
# 初始函數 __init___ -> 可以在類別裡定義初始函數
# __init__(第一個（一定要有）self）
# 初始函數 每當創建物件的時候都會被呼叫

# class Phone:
#         def __init__(self):
#                 print("初始函數")

# class Phone:
#         def __init__(self, number, price, waterproof):
#                 self.number = number
#                 self.price = price
#                 self.waterproof = waterproof
#
# phone1 = Phone("ABC123", 8000, True)
# print(phone1.number)
# print(phone1.price)
# print(phone1.waterproof)
#
# phone2 = Phone("CCC333", 87878, False)
# phone2.year = 2018
# phone2.number = "AAA111"
# print(phone2.number)
# print(phone2.price)
# print(phone2.waterproof)
# print(phone2.year)


#========================================
#class裡的函數 = 方法 method


# class Phone:
#         def __init__(self, number, price, waterproof, power):
#                 self.number = number
#                 self.price = price
#                 self.waterproof = waterproof
#                 self.power = power
#
#         def play(self, num):
#                 self.power -= num
#                 if self.power < 0:
#                         self.power = 0
#
#
# phone1 = Phone("ABC123", 8000, True, 60)
# print(phone1.power)
# phone1.play(70)
# print(phone1.power)
#
# phone2 = Phone("CCC333", 87878, False, 90)
# print(phone2.power)
# phone2.play(50)
# print(phone2.power)

#==========below is test 1================

# class Question:
#     def __init__(self, description, answer):
#         self.description = description
#         self.answer = answer
#
#     def ask(self):
#         ans = input(self.description)
#         if ans == self.answer:
#             return True
#         else:
#             return False
#
# question = Question("請問1+1=?\n"
#                     "(a)2\n"
#                     "(b)3\n"
#                     "(c)4\n"
#                     "(d)5\n", "a")
#
# if question.ask():
#         print("恭喜答對！🥳")
# else:
#         print(f"答錯了🐥！答案是：({question.answer})")

#===============below is test 2======================
class Question:
    def __init__(self, description, answer):
        self.description = description
        self.answer = answer

    def ask(self):
        ans = input(self.description)
        if ans == self.answer:
            return True
        else:
            return False

class QuestionGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        for i in range(0, len(questions)):
            print(questions[i].description)
            ans = input("請問答案為：")
            if ans == questions[i].answer:
                self.score += 1
                print("答對了！🥳\n")
            else:
                print(f"答錯了🐥🐥🐥！答案是{questions[i].answer}\n")
        print(f"共答對了{self.score}題")


question1 = Question("請問１＋１＝？\n(a) 2\n(b) 3\n(c) 4\n", "a")
question2 = Question("請問２＋２＝？\n(a) 2\n(b) 3\n(c) 4\n", "c")
question3 = Question("請問４＋４＝？\n(a) 7\n(b) 8\n(c) 9\n", "b")
questions = [question1, question2, question3]

question_game = QuestionGame(questions)

question_game.play()

#===============QuesrionGame solution from teacher======================

# class QuestionGame:
#     def __init__(self, questions):
#         self.question = questions
#         self.score = 0
#     def play(self):
#         for question in self.question:
#             if question.ask():
#                 self.score += 1
#                 print("恭喜答對\n")
#             else:
#                 print(f"答錯了，答案為{question.answer}\n")
#         print(f"共答對了{self.score}題")

