import pygame

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.speedy = 5
        self.score = 0

    def update(self, hand, height):
        self.hand = hand
        keys = pygame.key.get_pressed()
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > height:
            self.y = height - self.height
        elif self.hand == "L":
            if keys[pygame.K_w]:
                self.y -= self.speedy
            if keys[pygame.K_s]:
                self.y += self.speedy
        elif self.hand == "R":
            if keys[pygame.K_UP]:
                self.y -= self.speedy
            if keys[pygame.K_DOWN]:
                self.y += self.speedy

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))