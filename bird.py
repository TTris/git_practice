import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, imgs):
        super().__init__()
        self.x = x
        self.y = y
        self.imgs = imgs
        self.img_index = 0
        self.image = self.imgs[self.img_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.last_pic_time = pygame.time.get_ticks()
        self.img_frequency = 100
        self.speedy = 0

    def update(self, down_speed, ground_top):
        # 飛翔動畫
        now = pygame.time.get_ticks()
        if now - self.last_pic_time > self.img_frequency:
            self.img_index += 1
            if self.img_index >= len(self.imgs):
                self.img_index = 0
            self.image = pygame.transform.rotate(self.imgs[self.img_index], -self.speedy*2.5)
            self.last_pic_time = now

        # 引力
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.speedy = -10
            self.y += self.speedy
            self.rect.center = (self.x, self.y)
        else:
            self.speedy += down_speed
            if self.speedy > 11:
                self.speedy = 11
            self.y += self.speedy
            self.rect.center = (self.x, self.y)
        if self.rect.bottom > ground_top:
            self.rect.bottom = ground_top



    def reset(self):
        self.last_pic_time = pygame.time.get_ticks()














