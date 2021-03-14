import json
from game_score import Score

class GameStats:
    def __init__(self):
        self.game_active = False
        self.highscore = 0
        self.reset_stats()
        self.alltimescore = 0
        self.alltime_score()

    def reset_stats(self):
        self.ship_left = 3
        self.level_up = True
        self.score = 0
        self.level = 0

    def check_highscore(self):
        if  self.score > self.highscore:
            self.highscore = self.score

    def check_alltimescore(self):
        if self.highscore > self.alltimescore:
            self.alltime_score = self.highscore
            self.update_alltime_score()

    def alltime_score(self):
        filename = "alltimescore.json"
        with open(filename) as score:
            score_number = json.load(score)
            self.alltimescore = score_number
    
    def update_alltime_score(self):
        filename = "alltimescore.json"
        with open(filename,"w") as score:
            json.dump(self.alltime_score, score)
