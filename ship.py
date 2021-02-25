import pygame

class Ship:
    def __init__(self,game):
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.settings = game.settings()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.rect.midleft = self.screen_rect.midleft
        self.up_movement = False
        self.down_movement = False
    
    def movement(self):
        if self.up_movement:
            if self.rect.y >= self.screen_rect.height:
                self.rect.y +=  self.settings.ship_speed
        if self.down_movement:
            if self.down_movement:
                self.rect.y <= 0:
                    self.rect.y += -self.settings.ship_speed
    def blitme(self):
        self.screen_rect.blit(self.image,self.rect)