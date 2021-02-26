import pygame
import sys
from settings import Settings
from ship import Ship   

class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.backgroundcolor = self.settings.backgroundcolor
        self.screen = pygame.display.set_mode((1200,600))
        self.screen_rect = self.screen.get_rect()
        self.ship = Ship(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            if event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _check_keydown(self,keydown):
        if keydown.key == pygame.K_q:
            sys.exit() 
        if keydown.key == pygame.K_UP:
            self.ship.up_movement = True
        if keydown.key == pygame.K_DOWN:
            self.ship.down_movement = True
    def _check_keyup(self,keyup):
        if keyup.key == pygame.K_UP:
            self.ship.up_movement = False
        if keyup.key == pygame.K_DOWN:
            self.ship.down_movement = False
    def _update_game(self):
        self.screen.fill(self.backgroundcolor)
        self.ship.movement()
        self.ship.blitme()
        pygame.display.flip()
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_game()

if __name__ == "__main__":
    m = Main()
    m.run_game()
