# input
# 7
# 35
# output
# 49 26 27 28 29 30 31
# 48 25 10 11 12 13 32
# 47 24 9 2 3 14 33
# 46 23 8 1 4 15 34
# 45 22 7 6 5 16 35
# 44 21 20 19 18 17 36
# 43 42 41 40 39 38 37
# 5 7

# 수학적으로 풀 수 있지 않을까? 했지만 그냥 구현으로 해보자..
N = int(input())
T = int(input())
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
board = [[0 for _ in range(N)] for _ in range(N)]
dir = 0
curr = (0, 0)
for i in range(N**2):
    x, y = curr
    board[x][y] = str(N**2-i)
    if board[x][y] == str(T):
        T = f'{x+1} {y+1}'
    xx, yy = x+dx[dir], y+dy[dir]
    if xx < 0 or xx >= N or yy < 0 or yy >= N or board[xx][yy] != 0:
        dir = (dir+1) % 4
    curr = (x+dx[dir], y+dy[dir])
for b in board:
    print(' '.join(b))
print(T)