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
        self.alien_bullets = pygame.sprite.Group()
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_normal_button(mouse_pos)
                self.check_hard_button(mouse_pos)
                self.check_expert_button(mouse_pos)
                self.check_resetscore_button(mouse_pos)
                self.check_bulletmode(mouse_pos)
                
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

    def check_normal_button(self,position):
        collision = self.buttons.normal_rect.collidepoint(position)
        if collision and self.stats.game_active == False:
            self.stats.game_active = True

    def create_alien_bullets(self):
        if len(self.alien_bullets) == 0:
            bullet = Bullet(self)
            bullet_space = bullet.rect.height * 10
            screen_space = self.screen_rect.width//bullet_space
            for number in range(screen_space):
                projectile = Bullet(self)
                projectile.x_cord = self.screen_rect.center[0] 
                projectile.y_cord =  100 + projectile.rect.width * 10 * number
                projectile.rect.x = projectile.x_cord
                projectile.rect.y = projectile.y_cord
                self.alien_bullets.add(projectile)
    
    def check_hard_button(self,position):
        collision = self.buttons.hard_rect.collidepoint(position)
        if collision and self.stats.game_active == False:
            self.stats.game_active = True
            self.settings.alien_speed = 6
            self.settings.alien_drop_speed = -6
            self.settings.ship_speed = 7

    def check_expert_button(self,position):
        collision = self.buttons.expert_rect.collidepoint(position)
        if collision and self.stats.game_active == False:
            self.stats.game_active = True
            self.settings.alien_speed = 9
            self.settings.alien_drop_speed = -9
            self.settings.ship_speed = 10
    
    def check_resetscore_button(self, position):
        colision = self.buttons.reset_rect.collidepoint(position)
        if colision and self.stats.game_active == False:
            self.stats.alltimescore = 0
            self.stats.update_alltime_score()
            self.score.prep_alltimescore()

    def check_bulletmode(self, position):
        collision = self.buttons.bullet_rect.collidepoint(position)
        if collision and self.stats.game_active == False:
            if self.settings.bullet_mode:
                self.settings.bullet_mode = False
                self.buttons.show_button()
            else:
                self.settings.bullet_mode = True
                self.buttons.show_button()
        
    def _collisions(self):
        for bullet in self.bullets.copy():
            if pygame.sprite.spritecollide(bullet,self.aliens,True):
                self.bullets.empty()
                self.stats.score += self.settings.points
                self.stats.check_highscore()
                self.stats.check_alltimescore()
                self.score.prep_alltimescore()
                self.score.prep_highscore()
                self.score.prep_score()
    
    def alien_bullet_collision(self):
        for bullet in self.alien_bullets.copy():
            collide = bullet.rect.colliderect(self.ship)
            if collide:
                self._reset_game()


    def _fire_bullet(self):
        if len(self.bullets) <= self.settings.bullet_limit:
            new_bullet = Bullet(self)
            new_bullet.rect.center = self.ship.rect.center
            self.bullets.add(new_bullet)
            
    def _drop_alien(self):
        for alien in self.aliens:
            alien.x_cord += self.settings.alien_drop_speed
            alien.rect.x = alien.x_cord

    def level_up(self):
        if len(self.aliens) == 0 and self.stats.level_up:
            self._add_alien()
            self.settings.speed_up() 
            self.stats.level += 1
            self.score.prep_levels()
        elif len(self.aliens) == 0:
            self._add_alien()
            self.stats.level_up = True

            

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
                
        self.level_up()
        if check_edges != 0:
            if self.settings.bullet_mode:
                self.create_alien_bullets()
            self._drop_alien()
            self.settings.alien_direction = check_edges


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

    
    def _update_alienbullets(self):
        self.alien_bullets.update()
        for bullet in self.alien_bullets.copy():
            bullet.update_reverse()
            bullet.draw_bullet()
            print(self.alien_bullets)
            if bullet.rect.x <= 0:
                self.alien_bullets.remove(bullet)



    def _reset_game(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left += -1
            self.ship.reset_ship()
            self.score.prep_ships()
            self.stats.level_up = False
            self.aliens.empty() 
            self.bullets.empty()
            self.alien_bullets.empty()
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.aliens.empty()
            self.bullets.empty()
            self.ship.reset_ship()
            self.stats.reset_stats()
            self.score.prep_score()
            self.score.prep_levels()
            self.score.prep_ships()
            self.buttons.show_button()
            self.settings.change_dynamic_settings()
            self.alien_bullets.empty()
    
    def _update_game(self):
        self.screen.fill(self.backgroundcolor)

    def update_objects(self):
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.score.display_stats()
        self._update_bullet()
        self._update_alienbullets()
    
    def update_movement_collision(self):
        self.ship.movement()
        self._move_aliens()
        self._collisions()
        self.alien_bullet_collision()

    def run_game(self):
        while True:
            self._check_events()
            self._update_game()
            if self.stats.game_active:
                self.update_objects()
                self.update_movement_collision()
            if not self.stats.game_active:
                self.buttons.show_button()
            pygame.display.flip()


if __name__ == "__main__":
    m = Main()
    m.run_game()
