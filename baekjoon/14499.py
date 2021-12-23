# input
# 4 2 0 0 8
# 0 2
# 3 4
# 5 6
# 7 8
# 4 4 4 1 3 3 3 2
# output
# 0
# 0
# 3
# 0
# 0
# 8
# 6
# 3

N, M, x, y, K = map(int, input().split(" "))

class Dice:
    def __init__(self):
        self.top = 0
        self.bottom = 0
        self.east = 0
        self.west = 0
        self.south = 0
        self.north = 0
    
    def move(self, num):
        if num == 1:
            self.go_east()
        elif num == 2:
            self.go_west()
        elif num == 3:
            self.go_north()
        else:
            self.go_south()
    
    def go_east(self):
        self.top, self.bottom, self.east, self.west = self.west, self.east, self.top, self.bottom
    
    def go_west(self):
        self.top, self.bottom, self.east, self.west = self.east, self.west, self.bottom, self.top
    
    def go_north(self):
        self.top, self.bottom, self.south, self.north = self.south, self.north, self.bottom, self.top

    def go_south(self):
        self.top, self.bottom, self.south, self.north = self.north, self.south, self.top, self.bottom

dice = Dice()

board = [list(map(int, input().split(" "))) for _ in range(N)]

com = list(map(int, input().split(" ")))

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

curr_loc = [x, y]

for c in com:
    xx, yy = curr_loc[0]+dx[c-1], curr_loc[1]+dy[c-1]
    if not (0 <= xx < N) or not (0 <= yy < M):
        continue
    curr_loc = [xx, yy]
    dice.move(c)
    if board[xx][yy] == 0:
        board[xx][yy] = dice.bottom
    elif board[xx][yy] != 0:
        dice.bottom = board[xx][yy]
        board[xx][yy] = 0
    print(dice.top)
