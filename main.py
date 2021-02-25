import pygame
from settings import Settings

class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.backgroundcolor = self.settings.backgroundcolor
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()