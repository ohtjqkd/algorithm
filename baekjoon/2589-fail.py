# input
# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW
# output: 8
from collections import defaultdict
import heapq

L, W = map(int, input().split(" "))
board = [list(input()) for _ in range(L)]
edges = defaultdict(list)
memo = [[0 for _ in range(W)] for _ in range(L)]
di, dj = [0, 0, 1, -1], [1, -1, 0, 0]
dir = list(zip(di, dj))
for i in range(L):
    for j in range(W):
        if board[i][j] == "L":
            for d in dir:
                ii, jj = i+d[0], j+d[1]
                if 0 <= ii < L and 0 <= jj < W and board[ii][jj] == "L":
                    edges[(i,j)].append((ii, jj))
def max_dist(x, y, L, W, edges):
    distances = [[float('inf') for _ in range(W)] for _ in range(L)]
    distances[x][y] = 0
    heap = []
    max_d = 0
    heapq.heappush(heap, (0, x, y))
    while heap:
        w, x, y = heapq.heappop(heap)
        for nx, ny in edges.get((x,y), []):
            if memo[nx][ny] == 1:
                continue
            if distances[nx][ny] > w+1:
                heapq.heappush(heap, (w+1, nx, ny))
                distances[nx][ny] = w+1
    print(distances)
    return max_d
ret = 0
for i in range(L):
    for j in range(W):
        if board[i][j] == "L" and memo[i][j] == 0:
            memo[i][j] = 1
            ret = max([ret, max_dist(i, j, L, W, edges)])
print(ret)