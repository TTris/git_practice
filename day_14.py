# # 動畫遊戲 第三方套件 pygame
# # 基本架構
#
# import pygame
#
# # 工程師小習慣？！ 如果變數的值是不能做更改的，就會把變數設定成全大寫
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# WIDTH = 700
# HEIGHT = 500
# FPS = 60 #每秒鐘更新的畫面（跑的迴圈）Frames per second
#
#
# # 初始遊戲 一定要寫
# pygame.init()
#
# # 創建視窗 width, height
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("乒乓球")
#
#
# # 避免每台電腦效能不一，造成不同的遊戲效果，可用time.Clock() 去限制
# clock = pygame.time.Clock()
#
# # pygame 沒有mainloop迴圈自動偵測，所以要自己寫
# run = True
# x = 0
#
# while run:
#     clock.tick(FPS) #限制這個迴圈在１秒鐘內最多只能執行xxx次
#     # 取得輸入
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     # 遊戲更新
#     x += 10
#
#     # 畫面顯示
#         # fill背景色，三個參數 = 中的三原色 R,G,B，也可以寫調色盤的編碼
#     window.fill(BLACK)
#         # draw.rect 可以畫一個矩型 參數1:要畫在哪個視窗上；參數2:顏色；參數3:四個值，矩型座標x, y、寬度高度
#     pygame.draw.rect(window, WHITE, (x, 100, 100, 100))
#         # draw.circle 可以畫圓型 參數1:要畫在哪個視窗上；參數2:顏色；參數3:兩個值，矩型座標x, y；參數4: 半徑
#     pygame.draw.circle(window, WHITE, (400, 400), 50)
#
#     pygame.display.update() # 要寫這個才會顯示出來
#
#
#
# # 結束遊戲 一定要寫
# pygame.quit()

#===========================================================================
#
# import pygame
# from ball import Ball
#
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# WIDTH = 700
# HEIGHT = 500
# FPS = 60
#
# pygame.init()
#
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("乒乓球")
#
# ball = Ball(WIDTH/2, HEIGHT/2, 10, WHITE)
# ball1 = Ball(100, 100, 10, (255, 0, 0))
# ball2 = Ball(200, 200, 10, (0, 0, 255))
# ball3 = Ball(300, 300, 10, (0, 255, 0))
# ball4 = Ball(150, 200, 10, "#FFC1E0")
# ball5 = Ball(300, 400, 10, "#9F35FF")
#
#
# clock = pygame.time.Clock()
#
#
# run = True
# x = 0
#
# while run:
#     clock.tick(FPS)
#     # 取得輸入
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     # 遊戲更新
#     ball.update(WIDTH, HEIGHT)
#     ball1.update(WIDTH, HEIGHT)
#     ball2.update(WIDTH, HEIGHT)
#     ball3.update(WIDTH, HEIGHT)
#     ball4.update(WIDTH, HEIGHT)
#     ball5.update(WIDTH, HEIGHT)
#
#     # 畫面顯示
#     window.fill(BLACK)
#     ball.draw(window)
#     ball1.draw(window)
#     ball2.draw(window)
#     ball3.draw(window)
#     ball4.draw(window)
#     ball5.draw(window)
#     pygame.display.update()
#
#
#
#
# pygame.quit()

#=============================below is test 1==============================================

# import pygame
# from ball import Ball
# from paddle import Paddle
#
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# WIDTH = 700
# HEIGHT = 500
# FPS = 60
#
# pygame.init()
#
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("乒乓球")
#
# ball = Ball(WIDTH/2, HEIGHT/2, 10, WHITE)
# ball1 = Ball(100, 100, 10, (255, 0, 0))
# ball2 = Ball(200, 200, 10, (0, 0, 255))
# ball3 = Ball(300, 300, 10, (0, 255, 0))
# ball4 = Ball(150, 200, 10, "#FFC1E0")
# ball5 = Ball(300, 400, 10, "#9F35FF")
#
# paddle_width = 15
# paddle_height = 100
# left_paddle = Paddle(10, HEIGHT/2-paddle_height/2, paddle_width, paddle_height, WHITE)
# right_paddle = Paddle(WIDTH-10-paddle_width, HEIGHT/2-paddle_height/2,paddle_width, paddle_height, WHITE)
#
#
#
# clock = pygame.time.Clock()
#
#
# run = True
# x = 0
#
# while run:
#     clock.tick(FPS)
#     # 取得輸入
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     # 遊戲更新
#     ball.update(WIDTH, HEIGHT)
#     ball1.update(WIDTH, HEIGHT)
#     ball2.update(WIDTH, HEIGHT)
#     ball3.update(WIDTH, HEIGHT)
#     ball4.update(WIDTH, HEIGHT)
#     ball5.update(WIDTH, HEIGHT)
#
#     # 畫面顯示
#     window.fill(BLACK)
#     ball.draw(window)
#     ball1.draw(window)
#     ball2.draw(window)
#     ball3.draw(window)
#     ball4.draw(window)
#     ball5.draw(window)
#     left_paddle.draw(window)
#     right_paddle.draw(window)
#     pygame.display.update()
#
#
#
#
# pygame.quit()


#==========================================================================
# 取得輸入

#
# import pygame
# from ball import Ball
# from paddle import Paddle
#
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# WIDTH = 700
# HEIGHT = 500
# FPS = 60
#
# pygame.init()
#
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("乒乓球")
#
# ball = Ball(WIDTH/2, HEIGHT/2, 10, WHITE)
# ball1 = Ball(100, 100, 10, (255, 0, 0))
# ball2 = Ball(200, 200, 10, (0, 0, 255))
# ball3 = Ball(300, 300, 10, (0, 255, 0))
# ball4 = Ball(150, 200, 10, "#FFC1E0")
# ball5 = Ball(300, 400, 10, "#9F35FF")
#
# paddle_width = 15
# paddle_height = 100
# left_paddle = Paddle(10, HEIGHT/2-paddle_height/2, paddle_width, paddle_height, WHITE)
# right_paddle = Paddle(WIDTH-10-paddle_width, HEIGHT/2-paddle_height/2,paddle_width, paddle_height, WHITE)
#
#
#
# clock = pygame.time.Clock()
#
#
# run = True
# x = 0
# y = 100
#
# while run:
#     clock.tick(FPS)
#     # 取得輸入
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         # elif event.type == pygame.KEYDOWN:  # KEYDOWN 函數可判斷某鍵是否有被按下
#         #     if event.key == pygame.K_a:     # K_a 表示A鍵被按下. 數字直接為數字、上下左右為：UP, DOWN, LEFT, RIGHT、空白為Space
#         #         print("按了Ａ")
#         #     elif event.key == pygame.K_UP:
#         #         y -= 4
#         #     elif event.key == pygame.K_DOWN:
#         #         y += 4
#     keys = pygame.key.get_pressed()  # 這個 pygame.key.get_pressed() 函數會提供布林值，來看鍵盤上的案件是否被按住
#     if keys[pygame.K_UP]:            # 這樣寫代表，若「上」鍵被按住，會一直回傳True
#         y -=4
#     if keys[pygame.K_DOWN]:
#         y += 4
#
#
#     # 遊戲更新
#     ball.update(WIDTH, HEIGHT)
#     ball1.update(WIDTH, HEIGHT)
#     ball2.update(WIDTH, HEIGHT)
#     ball3.update(WIDTH, HEIGHT)
#     ball4.update(WIDTH, HEIGHT)
#     ball5.update(WIDTH, HEIGHT)
#
#     # 畫面顯示
#     window.fill(BLACK)
#     ball.draw(window)
#     ball1.draw(window)
#     ball2.draw(window)
#     ball3.draw(window)
#     ball4.draw(window)
#     ball5.draw(window)
#     left_paddle.draw(window)
#     right_paddle.draw(window)
#     pygame.draw.rect(window, WHITE, (100, y, 100, 100))
#     pygame.display.update()
#
#
#
#
# pygame.quit()

#======================= below is test 2==================================================
#
# import pygame
# from ball import Ball
# from paddle import Paddle
#
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# WIDTH = 700
# HEIGHT = 500
# FPS = 60
#
# pygame.init()
#
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("乒乓球")
#
# ball = Ball(WIDTH/2, HEIGHT/2, 10, WHITE)
# ball1 = Ball(100, 100, 10, (255, 0, 0))
# ball2 = Ball(200, 200, 10, (0, 0, 255))
# ball3 = Ball(300, 300, 10, (0, 255, 0))
# ball4 = Ball(150, 200, 10, "#FFC1E0")
# ball5 = Ball(300, 400, 10, "#9F35FF")
#
# paddle_width = 15
# paddle_height = 100
# left_paddle = Paddle(10, HEIGHT/2-paddle_height/2, paddle_width, paddle_height, WHITE)
# right_paddle = Paddle(WIDTH-10-paddle_width, HEIGHT/2-paddle_height/2,paddle_width, paddle_height, WHITE)
#
#
#
# clock = pygame.time.Clock()
#
#
# run = True
# x = 0
# y = 100
#
# while run:
#     clock.tick(FPS)
#     # 取得輸入
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     left_paddle.update("L", HEIGHT)
#     right_paddle.update("R", HEIGHT)
#
#
#     # 遊戲更新
#     ball.update(WIDTH, HEIGHT)
#     ball1.update(WIDTH, HEIGHT)
#     ball2.update(WIDTH, HEIGHT)
#     ball3.update(WIDTH, HEIGHT)
#     ball4.update(WIDTH, HEIGHT)
#     ball5.update(WIDTH, HEIGHT)
#
#     # 畫面顯示
#     window.fill(BLACK)
#     ball.draw(window)
#     ball1.draw(window)
#     ball2.draw(window)
#     ball3.draw(window)
#     ball4.draw(window)
#     ball5.draw(window)
#     left_paddle.draw(window)
#     right_paddle.draw(window)
#     pygame.display.update()
#
#
#
#
# pygame.quit()


#========================================================================
# 顯示文字
# Step 1: 準備字體
# Step 2: 用 pygame.font.Font()載入。 參數兩個：字體路徑、字體大小
# Step 3: 用 font.render()設定。      參數三個：要顯示的文字、是否抗鋸齒、顏色
# Step 4: 用 window.blit()來顯示文字。 參數兩個：文字、座標（文字左上角的座標）
#
#
#
# import pygame
# from ball import Ball
# from paddle import Paddle
#
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# WIDTH = 700
# HEIGHT = 500
# FPS = 60
#
# pygame.init()
#
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("乒乓球")
# font = pygame.font.Font("微軟正黑體.ttf", 50)
# text = font.render("你好", True, WHITE)      #要顯示的文字、是否抗鋸齒、顏色
#
#
# ball = Ball(WIDTH/2, HEIGHT/2, 10, WHITE)
# ball1 = Ball(100, 100, 10, (255, 0, 0))
# ball2 = Ball(200, 200, 10, (0, 0, 255))
# ball3 = Ball(300, 300, 10, (0, 255, 0))
# ball4 = Ball(150, 200, 10, "#FFC1E0")
# ball5 = Ball(300, 400, 10, "#9F35FF")
#
# paddle_width = 15
# paddle_height = 100
# left_paddle = Paddle(10, HEIGHT/2-paddle_height/2, paddle_width, paddle_height, WHITE)
# right_paddle = Paddle(WIDTH-10-paddle_width, HEIGHT/2-paddle_height/2,paddle_width, paddle_height, WHITE)
#
#
#
# clock = pygame.time.Clock()
#
#
# run = True
# x = 0
# y = 100
#
# while run:
#     clock.tick(FPS)
#     # 取得輸入
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     left_paddle.update("L", HEIGHT)
#     right_paddle.update("R", HEIGHT)
#
#
#     # 遊戲更新
#     ball.update(WIDTH, HEIGHT)
#     ball1.update(WIDTH, HEIGHT)
#     ball2.update(WIDTH, HEIGHT)
#     ball3.update(WIDTH, HEIGHT)
#     ball4.update(WIDTH, HEIGHT)
#     ball5.update(WIDTH, HEIGHT)
#
#     # 畫面顯示
#     window.fill(BLACK)
#     window.blit(text, (0, 0))  #文字、座標（文字左上角的座標）
#     ball.draw(window)
#     ball1.draw(window)
#     ball2.draw(window)
#     ball3.draw(window)
#     ball4.draw(window)
#     ball5.draw(window)
#     left_paddle.draw(window)
#     right_paddle.draw(window)
#     pygame.display.update()
#
# pygame.quit()


#===================project 14=====================================================
import pygame
from ball import Ball
from paddle import Paddle

def draw_score(window, left_score, right_score):
    left_score_text = score_font.render(f"{left_score}", True, WHITE)
    right_score_text = score_font.render(f"{right_score}", True, WHITE)
    window.blit(left_score_text, (WIDTH/2/2, 0))
    window.blit(right_score_text, (WIDTH/2/2+WIDTH/2, 0))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 700
HEIGHT = 500
FPS = 60

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("乒乓球")
score_font = pygame.font.Font("微軟正黑體.ttf", 50)




ball = Ball(WIDTH/2, HEIGHT/2, 10, WHITE)


paddle_width = 15
paddle_height = 100
left_paddle = Paddle(10, HEIGHT/2-paddle_height/2, paddle_width, paddle_height, WHITE)
right_paddle = Paddle(WIDTH-10-paddle_width, HEIGHT/2-paddle_height/2,paddle_width, paddle_height, WHITE)


clock = pygame.time.Clock()


run = True
x = 0
y = 100




while run:
    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    left_paddle.update("L", HEIGHT)
    right_paddle.update("R", HEIGHT)


    # 遊戲更新
    ball.update(WIDTH, HEIGHT,left_paddle, right_paddle)
    ball.check_collide(left_paddle, right_paddle)


    # 畫面顯示
    window.fill(BLACK)
    draw_score(window, left_paddle.score, right_paddle.score)
    ball.draw(window)
    left_paddle.draw(window)
    right_paddle.draw(window)
    pygame.display.update()


pygame.quit()
