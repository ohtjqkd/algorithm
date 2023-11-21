# input
# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2
# output
# 3
# 1 7 13

M, N, K = map(int, input().split(" "))
board = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split(" "))
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

def dfs(x, y, M, N, board):
    ret = 1
    dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]
    stack = [(x, y)]
    board[x][y] = 1
    while stack:
        (x, y) = stack.pop()
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < M and 0 <= yy < N and board[xx][yy] == 0:
                board[xx][yy] = 1
                stack.append((xx, yy))
                ret += 1
    return ret

section = 0
sizes = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            section += 1
            board[i][j] = 1
            sizes.append(dfs(i, j, M, N, board))
print(section)
print(' '.join(map(str, sorted(sizes))))
