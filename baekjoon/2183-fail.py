from collections import defaultdict
n, string = input().split(" ")
n = int(n)
set_score = defaultdict(int)
class Game:
    def __init__(self):
        self.score = defaultdict(int)
        self.first = -1
        self.second = -1

    def set_score(self, winner):
        if self.first != winner and self.score.get(self.first) == 4:
            self.score[self.first] -= 1
        else:
            self.score[winner] += 1
            if self.score[winner] > self.score.get(self.first):
                self.first = winner
            elif self.score[winner] > self.score.get(self.second):
                self.second = winner
    def is_gameset(self, winner):
        winner_score = self.score[winner]
        if winner_score == 4:
            self.reset()
            return True
        elif winner_score == 3 and self.score.get(self.second) <= 2:
            self.reset()
            return True
        return F
    
    def reset(self):
        self.score = defaultdict(int)
        self.first = -1
        self.second = -1

game = Game()    
for winner in string:
    if set_score[winner] == 3:
        print(winner)
        break
    else:
        if game.is_gameset(winner):
            set_score[winner] += 1
        else:
            game.set_score(winner)
