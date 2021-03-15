import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,game):
        super().__init__()
        self.settings= game.settings
        self.screen = game.screen
        self.rect = pygame.Rect(0,0,self.settings.bullet_height, self.settings.bullet_width)
        self.ship = game.ship
        self.x_cord = self.rect.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.settings.bullet_color,self.rect)

    def update(self):
        self.x_cord += self.settings.bullet_speed
        self.rect.x = self.x_cord
    
    def update_reverse(self):
        self.x_cord += self.settings.alien_bullet_speed
        self.rect.x = self.x_cord
        