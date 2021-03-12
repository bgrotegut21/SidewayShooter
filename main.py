import pygame
import sys
from time import sleep

from settings import Settings
from ship import Ship   
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from game_score import Score
from button import Buttons

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
        self.stats = GameStats()
        self.score = Score(self)
        self.buttons = Buttons(self)

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
    def _collisions(self):
        for bullet in self.bullets.copy():
            if pygame.sprite.spritecollide(bullet,self.aliens,True):
                self.bullets.empty()
                self.stats.score += self.settings.points
                self.score.prep_score()
            
    def _fire_bullet(self):
        if len(self.bullets) <= self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _drop_alien(self):
        for alien in self.aliens:
            alien.x_cord += self.settings.alien_drop_speed
            alien.rect.x = alien.x_cord

    def _move_aliens(self):
        check_edges = 0
        self.aliens.update()
        for alien in self.aliens:
            alien.update()
            if alien.rect.y <= 0:
                check_edges = 1
            if alien.rect.y >= self.screen_rect.height - alien.rect.height:
                check_edges = -1
            if alien.rect.x <= 0:
                self._reset_game()
        if check_edges != 0:
            self._drop_alien()
            self.settings.alien_direction = check_edges
        if len(self.aliens) == 0 and self.stats.level_up:
            self._add_alien()
            self.settings.speed_up() 
            self.stats.level += 1
            self.score.prep_levels()
        elif len(self.aliens) == 0:
            self._add_alien()
            self.stats.level_up = True

        if pygame.sprite.spritecollide(self.ship,self.aliens,True):
            self._reset_game()  

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            bullet.draw_bullet()
            bullet.update()
            if bullet.rect.x >= self.screen_rect.width:
                self.bullets.remove(bullet)
                self.settings.current_bullets = self.settings.bullet_limit

    def _reset_game(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left += -1
            self.ship.reset_ship()
            self.score.prep_ships()
            self.stats.level_up = False
            self.aliens.empty() 
            self.bullets.empty()
            
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.stats.reset_stats()
            self.score.prep_score()
            self.score.prep_levels()
            
    
    def _update_game(self):
        self.screen.fill(self.backgroundcolor)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.score.display_stats()
        if self.stats.game_active:
            self._update_bullet()
        pygame.display.flip()
    
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.movement()
                self._move_aliens()
                self._collisions()
            else:
                self.buttons.show_button()
            self._update_game()


if __name__ == "__main__":
    m = Main()
    m.run_game()
