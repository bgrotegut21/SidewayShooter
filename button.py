import pygame

class Buttons:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(None,48)

        self.normal_button("Normal")
        self.hard_button("Hard")
        self.expert_button('Expert')
        self.reset_score("Reset Alltime Score")
        self.bullet_mode("Bullet Mode - On")



    
    def normal_button(self,msg):
        self.nromal_img = self.font.render(msg,True, self.settings.button_text_color,(0,255,0))
        self.normal_rect = self.nromal_img.get_rect()
        self.normal_rect.x = self.screen_rect.center[0]
        self.normal_rect.y = self.screen_rect.center[1] - 100
    
    def hard_button(self,msg):
        self.hard_img = self.font.render(msg,True, self.settings.button_text_color,(255,0,0))
        self.hard_rect = self.hard_img.get_rect()
        self.hard_rect.x = self.screen_rect.center[0]
        self.hard_rect.y = self.screen_rect.center[1] - 50
    
    def expert_button(self,msg):
        self.expert_img = self.font.render(msg,True, self.settings.button_text_color,(0,0,255))
        self.expert_rect = self.expert_img.get_rect()
        self.expert_rect.x = self.screen_rect.center[0]
        self.expert_rect.y = self.screen_rect.center[1]

    def reset_score(self, msg):
        self.reset_img = self.font.render(msg,True, self.settings.button_text_color,(0,0,0))
        self.reset_rect = self.reset_img.get_rect()
        self.reset_rect.x = self.screen_rect.center[0]
        self.reset_rect.y = self.screen_rect.center[1] + 50
    
    def bullet_mode(self, msg):
        self.bullet_img = self.font.render(msg,True, self.settings.button_text_color,(255,0,0))
        self.bullet_rect = self.bullet_img.get_rect()
        self.bullet_rect.x = self.screen_rect.center[0]
        self.bullet_rect.y = self.screen_rect.center[1] + 100
    
    def show_button(self):
        self.screen.blit(self.nromal_img,self.normal_rect)
        self.screen.blit(self.hard_img, self.hard_rect)
        self.screen.blit(self.expert_img, self.expert_rect)
        self.screen.blit(self.reset_img, self.reset_rect)
        self.screen.blit(self.bullet_img, self.bullet_rect)