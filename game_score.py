import pygame
from pygame.sprite import Sprite
class Score(Sprite):

    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = game.stats
        self.font = pygame.font.Font(None,32)
        self.prep_score()
        self.prep_levels()
    
    def truncate(self,n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    def prep_score(self):
        rounded_score_number = self.truncate(self.stats.score,-2)
        score_number = "{:,}".format(int(rounded_score_number))
        self.score_text = self.font.render(str(score_number),True,(0,0,0))
        self.score_rect = self.score_text.get_rect()
        self.score_rect.x = self.screen_rect.topright[0] - 100
        self.score_rect.y = self.screen_rect.topright[1]

    def prep_levels(self):
        level_number = "{:,}".format(self.stats.level)
        self.level_text = self.font.render(str(level_number), True, (0,0,0))
        self.level_rect = self.level_text.get_rect()
        self.level_rect.x = self.screen_rect.topleft[0] + 20
        self.level_rect.y = self.screen_rect.topright[1] 
        
    def display_stats(self):
        self.screen.blit(self.score_text,self.score_rect)
        self.screen.blit(self.level_text, self.level_rect)
    
    
