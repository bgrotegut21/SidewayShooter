from game_stats import GameStats
class Settings:
    def __init__(self):
        self.backgroundcolor = (233,233,233)

        self.bullet_speed = 3
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_limit = 1
        self.current_bullets = 0
        self.bullet_color = (0,0,0)
        self.stats = GameStats()
        
        self.alien_direction = -1
        self.number_columns = 6
        self.scale = 1.5

        self.button_width = 150
        self.button_height = 50
        self.button_text_color = (233,233,233)

        self.change_dynamic_settings()

    def change_dynamic_settings(self):
        self.ship_speed = 10
        self.alien_speed = 10
        self.points = 50
        self.alien_drop_speed = -3

    def speed_up(self):
        self.ship_speed *= self.scale
        self.alien_speed *= self.scale
        self.alien_drop_speed *= self.scale
        self.points = int(self.points) * int(self.scale)
        self.stats.level += 1
