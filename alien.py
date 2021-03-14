import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,game):
        super().__init__()
        self.settings = game.settings
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.y_cord = self.rect.height
        self.x_position = self.screen_rect.width - self.rect.width
        self.x_cord = self.screen_rect.width - self.rect.width
        self.rect.x = self.x_cord
        self.rect.y = self.y_cord

    def update(self):
        self.y_cord += (self.settings.alien_speed * self.settings.alien_direction)
        self.rect.y = self.y_cord