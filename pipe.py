import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, img, top):
        super().__init__()
        self.x = x
        self.y = y
        self.top = top
        self.image = img
        self.rect = self.image.get_rect()
        self.bird_pass = False
        if top == True:
            self.rect.bottomleft = (self.x, self.y-75)
        else:
            self.rect.topleft = (self.x, self.y+75)

    def update(self, pipe_speed):
        self.x -= pipe_speed
        if self.rect.right < 0:
            self.kill()
        elif self.top == True:
            self.rect.midbottom = (self.x, self.y-75)
        else:
            self.rect.midtop = (self.x, self.y+75)







