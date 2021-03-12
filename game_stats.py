
class GameStats:
    def __init__(self):
        self.game_active = False
        
        self.reset_stats()
    def reset_stats(self):
        self.ship_left = 3
        self.level_up = True
        self.score = 0
        self.level = 0