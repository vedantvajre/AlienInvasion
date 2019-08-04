import pygame

from pygame.sprite import Sprite


class Aliens(Sprite):
    def __init__(self, ai_settings, screen):
        super(Aliens, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.rect.get_image()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = True
        self.moving_left = False
        self.moving_down = True

    def update(self):
        if  self.moving_right and self.rect.right > self.screen_rect.right:
            self.moving_right = False
            self.moving_left = True
        if  self.moving_left and self.rect.left > self.screen_rect.left:
            self.moving_right = True
            self.moving_left = False
        if self.moving_down and self.rect.bottom > self.screen_rect.bottom:
            self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
