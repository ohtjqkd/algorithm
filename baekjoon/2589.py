# input
# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW
# output: 8
# pypy3로 통과
from collections import deque

L, W = map(int, input().split(" "))
board = [list(input()) for _ in range(L)]
def bfs(x, y, dist):
    ret = 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    dist[x][y] = 0
    visited = set()
    visited.add((x, y))
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < L and 0 <= yy < W and board[xx][yy] == 'L' and (xx, yy) not in visited:
                visited.add((xx, yy))
                q.append((xx, yy))
                dist[xx][yy] = dist[x][y] + 1
                ret = max(ret, dist[xx][yy])
    return ret
ret = 0
dist = [[0 for _ in range(W)] for _ in range(L)]
for i in range(L):
    for j in range(W):
        if board[i][j] == "L":
            ret = max([ret, bfs(i, j, dist)])
print(ret)