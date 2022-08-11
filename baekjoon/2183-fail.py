# 아 이거 뭐야..

from collections import defaultdict
n, string = input().split(" ")
n = int(n)
set_score = defaultdict(int)
class TenisGame:
    def __init__(self, player):
        self.player = player
        self.set_game()
        self.set_set()
        self.set_point = [0] * player

    def up2int(s: str):
        return ord(s) - ord('A')
    
    def check_all_win(self):
        if sum(self.game_point) == 6:
            return 2
        return 1

    def set_score(self, winner: str):
        win_idx = self.up2int(winner)
        if self.score[win_idx] == 4:
            self.game_point[win_idx] += 1
            self.set_game()
            return True
        elif self.first != win_idx:
            if self.score[self.first] == 4:
                self.score[self.first]
            
        if self.first != winner and self.score.get(self.first) == 4:
            self.score[self.first] -= 1
        else:
            self.score[winner] += 1
            if self.score[winner] > self.score.get(self.first):
                self.first = winner
            elif self.score[winner] > self.score.get(self.second):
                self.second = winner

    
    def set_game(self):
        self.score = [0] * self.player
        self.first = -1
        self.second = -1
        self.score_sum = 0
    
    def set_set(self):
        self.game_point = [0] * self.player

game = TenisGame(n)    
for winner in string:
    
    if set_score[winner] == 3:
        print(winner)
        break
    else:
        if game.is_gameset(winner):
            set_score[winner] += 1
        else:
            game.set_score(winner)
