# input
# 3 1
# 21 21 80 80
# 41 41 60 60
# 71 71 90 90

# output
# 500

N, M = tuple(map(int, input().split(" ")))
ret = 0
board = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    x1, y1, x2, y2 = tuple(map(lambda x: int(x)-1, input().split(" ")))
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            board[i][j] += 1


for b in board:
    for n in b:
        if n > M:
            ret += 1
print(ret)