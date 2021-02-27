import pygame
import sys
from settings import Settings
from ship import Ship   
from bullet import Bullet
from alien import Alien
class Main:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.backgroundcolor = self.settings.backgroundcolor
        self.screen = pygame.display.set_mode((1200,600))
        self.screen_rect = self.screen.get_rect()
        self.bullets = pygame.sprite.Group()
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self._add_alien()

    def _add_alien(self):
        alien = Alien(self)
        alien_height = alien.rect.height
        screen_height = self.screen_rect.height
        screen_space = screen_height - (alien_height*2)
        number_of_aliens = screen_space//(alien_height*2)
        number_of_columns = self.settings.number_columns
        for column in range(number_of_columns):
            for aliens in range(number_of_aliens):
                new_alien = Alien(self)
                new_alien.x_cord = new_alien.x_position - (new_alien.rect.width *2) * column
                new_alien.y_cord = (new_alien.rect.height * 2) * aliens
                new_alien.rect.x = new_alien.x_cord
                new_alien.rect.y = new_alien.y_cord
                self.aliens.add(new_alien)
        
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
        if keydown.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup(self,keyup):
        if keyup.key == pygame.K_UP:
            self.ship.up_movement = False
        if keyup.key == pygame.K_DOWN:
            self.ship.down_movement = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _drop_alien(self):
        for alien in self.aliens:
            alien.y_cord = self.settings.alien_drop_speed
            alien.rect.y = alien.y_cord
    def _move_aliens(self):
        check_edges = 0
        self.aliens.update()
        for alien in self.aliens:
            alien.update()
            if alien.rect.y <= 0:
                check_edges = 1
            if alien.rect.y >= self.screen_rect.height - alien.rect.height:
                check_edges = -1
        if check_edges != 0:
            self._drop_alien
            self.settings.alien_direction = check_edges

    
    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            bullet.draw_bullet()
            bullet.update()
            if bullet.rect.x >= self.screen_rect.width:
                self.bullets.remove(bullet)

    def _update_game(self):
        self.screen.fill(self.backgroundcolor)
        self.ship.movement()
        self.ship.blitme()
        self._update_bullet()
        self._move_aliens()
        self.aliens.draw(self.screen)
        pygame.display.flip()
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_game()

if __name__ == "__main__":
    m = Main()
    m.run_game()
