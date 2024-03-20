import pygame
import random

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        radom_list = [-2, 2]
        self.speedx = random.choice(radom_list)
        self.speedy = random.choice(radom_list)

    def update(self, width, height, left_paddle, right_paddle):
        self.x += self.speedx
        self.y += self.speedy
        ball_top = self.y - self.radius
        ball_bottom = self.y + self.radius
        ball_left = self.x - self.radius
        ball_right = self.x + self.radius

        if ball_top < 0 or ball_bottom > height:
            self.speedy *= -1

        if ball_left < 0:
            right_paddle.score += 1
            self.reset(width, height)
        elif ball_right > width:
            left_paddle.score += 1
            self.reset(width, height)

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


    def reset(self, width, height):
        self.x = width / 2
        self.y = height / 2
        radom_list = [-2, 2]
        self.speedx = random.choice(radom_list)
        self.speedy = random.choice(radom_list)

    def check_collide(self, left_paddle, right_paddle):
        left_paddle_top = left_paddle.y
        left_paddle_bottom = left_paddle.y + left_paddle.height
        left_paddle_left = left_paddle.x
        left_paddle_right = left_paddle.x + left_paddle.width

        right_paddle_top = right_paddle.y
        right_paddle_bottom = right_paddle.y + right_paddle.height
        right_paddle_left = right_paddle.x
        right_paddle_right = right_paddle.x + right_paddle.width

        if self.speedx < 0:
            ball_left_x = self.x - self.radius
            ball_left_y = self.y

            if left_paddle_top < ball_left_y and\
                left_paddle_bottom > ball_left_y and \
                left_paddle_left < ball_left_x and\
                left_paddle_right > ball_left_x:
                self.speedx *= -1
                self.speedy += random.randint(-5, +5)

        else:
            ball_right_x = self.x + self.radius
            ball_right_y = self.y

            if right_paddle_top < ball_right_y and\
                right_paddle_bottom > ball_right_y and \
                right_paddle_left < ball_right_x and\
                right_paddle_right > ball_right_x:
                self.speedx *= -1
                self.speedy += random.randint(-5, +5)
