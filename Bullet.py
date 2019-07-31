import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, ship):
        pygame.sprite.Sprite.__init__(self, ai_settings, screen, ship)
        self.screen = screen
        self.ai_settings = ai_settings
        self.rect = pygame.Rect(0, 0, self.ai_settings.bullet_width,
                                self.ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.pos = float(self.rect.centerx)
        self.rect.midtop = ship.rect.midtop
        self.color = self.ai_settings.bullet_color

    def update(self):
        self.pos -= self.ai_settings.speed_factor
        self.rect.pos = self.pos

    def blitme(self):
        self.screen.blit(self.screen, self.color, self.rect)

