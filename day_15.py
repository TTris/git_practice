# import pygame
#
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# SCREEN_WIDTH = 780
# SCREEN_HEIGHT = 600
# FPS = 60
#
#
# pygame.init()
#
# window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("鳥鳥")
#
#
# clock = pygame.time.Clock()
#
# #載入圖片 pygame.image.load
# bg_img = pygame.image.load("img/bg.png")
# #調整圖片大小 pygame.transform.scale
# bg_img = pygame.transform.scale(bg_img, (780, 600))
#
#
# bird_img = pygame.image.load("img/bird1.png")
# # 旋轉圖片用 transform.rotate(要翻轉的圖片, 翻轉角度), 是逆時鐘旋轉
# # 翻轉圖片用 transform.flip(要翻轉的圖片,水平翻轉？True/False ,垂直翻轉？True/False)
#
# ground_img = pygame.image.load("img/ground.png")
# ground_speed = 4
# ground_x = 0
#
#
# pipe_img = pygame.image.load("img/pipe.png")
#
# pygame.display.set_icon(bird_img)
#
#
#
#
#
#
# run = True
# while run:
#     clock.tick(FPS)
#
#     # 取得輸入
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#
#     #遊戲更新
#     ground_x -= ground_speed
#     if ground_x < -100:
#         ground_x = 0
#
#
#     #畫面顯示
#     window.blit(bg_img, (0, 0))
#     window.blit(bird_img, (100, 100))
#     window.blit(pipe_img, (300, 400))
#     window.blit(ground_img, (ground_x, SCREEN_HEIGHT - 100))
#     pygame.display.update()
#
#
#
# pygame.quit()

#===================================================================
# # Class用法：inheritance 繼承
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print(f"你好我是{self.name}")
#
# class Student(Person):                       #繼承的方法就是在小括號寫上類別，相當於在Student中複製一份Person
#     def __init__(self, name, age, score):    #可以重新定義初始函數，取代Person中的初始函數
#         Person.__init__(self, name, age)     #可以呼叫已經設定好的初始函數
#         # super().__init__(name, age)        #此行寫法等同於上行寫法，差別在於，不用重複寫進"self"
#         self.score = score
#
#
# student1 = Student("小白", 23, 70)
# student1.say_hi()
#===================================================================
# 繼承Sprite類別
#===================================================================

import pygame
import random
from bird import Bird
from pipe import Pipe

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 780
SCREEN_HEIGHT = 600
FPS = 60


pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("鳥鳥")


clock = pygame.time.Clock()

bg_img = pygame.image.load("img/bg.png")
bg_img = pygame.transform.scale(bg_img, (780, 600))

ground_img = pygame.image.load("img/ground.png")
ground_speed = 4
ground_x = 0
pipe_frequency = 1500
last_pipe_time = pygame.time.get_ticks() - pipe_frequency
ground_top = SCREEN_HEIGHT-100

bird_imgs = []
for i in range(1,3):
    bird_imgs.append(pygame.image.load(f"img/bird{i}.png"))

pygame.display.set_icon(bird_imgs[0])

bird = Bird(100, 100, bird_imgs)
bird_group = pygame.sprite.Group()
bird_group.add(bird)

bird_down_speed = 0.5


pipe_img = pygame.image.load("img/pipe.png")
flip_pipe_img = pygame.transform.flip(pipe_img, False, True)

pipe_speed = 4
pipe_group = pygame.sprite.Group()

score = 0
score_font = pygame.font.Font("微軟正黑體.ttf", 50)

def create_pipe(last_pipe_time, pipe_frequency, pipe_group):
    now = pygame.time.get_ticks()
    random_height = random.randint(-120, 80)
    if now - last_pipe_time > pipe_frequency:
        pipe_btm = Pipe(SCREEN_WIDTH, SCREEN_HEIGHT / 2 + random_height, pipe_img, False)
        pipe_top = Pipe(SCREEN_WIDTH, SCREEN_HEIGHT / 2 + random_height , flip_pipe_img, True)
        pipe_group.add(pipe_btm)
        pipe_group.add(pipe_top)
        return now

    return last_pipe_time

def draw_score():
    score_text = score_font.render(str(score), True, WHITE)
    window.blit(score_text, (SCREEN_WIDTH/2, 20))

run = True
game_over = False

while run:
    clock.tick(FPS)

    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    #遊戲更新
    bird_group.update(bird_down_speed, game_over, ground_top)

    if not game_over:
        pipe_group.update(pipe_speed)
        last_pipe_time = create_pipe(last_pipe_time, pipe_frequency, pipe_group)
        # 判斷是否通過管子
        first_pipe = pipe_group.sprites()[0]
        if not first_pipe.bird_pass:
            if first_pipe.rect.right < bird.rect.left:
                score += 1
                first_pipe.bird_pass = True

        ground_x -= ground_speed
        if ground_x < -100:
            ground_x = 0


    #碰撞判斷 (後面兩個布林值代表，碰到後前群組/後群組要不要刪掉，回傳字典)
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) \
            or bird.rect.top <= 0 \
            or bird.rect.bottom >= ground_top:
        game_over = True




    #畫面顯示
    window.blit(bg_img, (0, 0))
    bird_group.draw(window)
    pipe_group.draw(window)
    window.blit(ground_img, (ground_x, ground_top))
    draw_score()
    pygame.display.update()



pygame.quit()

#===================================================================