import pygame

class Score:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = game.stats
        self.font = pygame.font.Font(None,48)
        self.prep_score()
        self.prep_levels()

    def prep_score(self):
        score_number = "{:,}".format(self.stats.score)
        self.score_text = self.font.render(str(score_number),True,(0,0,0))
        self.score_rect = self.score_text.get_rect()
        self.score_rect.x = self.screen_rect.topright[0] - 100
        self.score_rect.y = self.screen_rect.topright[1]
    def prep_levels(self):
        level_number = "{:,}".format(self.stats.level)
        self.level_text = self.font.render(str(level_number), True, (0,0,0))
        self.level_rect = self.level_text.get_rect()
        self.score_rect.x = self.screen_rect.topleft[0] - 20
        self.score_rect.y = self.screen_rect.topright[1] 
        
    def display_stats(self):
        self.screen.blit(self.score_text,self.score_rect)
        self.screen.blit(self.level_text, self.level_rect)
    