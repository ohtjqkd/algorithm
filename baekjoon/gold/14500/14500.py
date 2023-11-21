# 14500 테트로미노
from my_module.modules import print_board

N, M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
result = 0
for b in board:
    print(b)

horizon = [[0] * M for _ in range(N)]
vertical = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i != 0:
            vertical[i][j] = board[i][j] + board[i - 1][j]
        if j != 0:
            horizon[i][j] = board[i][j] + board[i][j - 1]

dir = [[]]

for i in range(N):
    for j in range(M):
        


print_board(horizon)
print_board(vertical)
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def back_tracking(x, y, visited, ret, cnt):
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if visited[xx][yy] == 1:
            return 
