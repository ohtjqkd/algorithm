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
di, dj = [0, 0, 1, -1], [1, -1, 0, 0]
dir = list(zip(di, dj))
for i in range(L):
    for j in range(W):
        if board[i][j] == "L":
            for d in dir:
                ii, jj = i+d[0], j+d[1]
                if 0 <= ii < L and 0 <= jj < W and board[ii][jj] == "L":
                    edges[(i,j)].append((ii, jj))
print(edges)
def max_dist(x, y, L, W, edges):
    distances = [[float('inf') for _ in range(W)] for _ in range(L)]
    distances[x][y] = 1
    heap = []
    heapq.heappush(heap, (0, x, y))
    while heap:
        w, x, y = heapq.heappop(heap)
        for nx, ny in edges.get((x,y), []):
            if distances[nx][ny] > w+1:
                heapq.heappush(heap, (w+1, nx, ny))
                distances[nx][ny] = w+1
    ret = max(sum(distances, []), key = lambda x: x if x != float('inf') else 0)
    return ret
ret = 0
for i in range(L):
    for j in range(W):
        if board[i][j] == "L":
            ret = max([ret, max_dist(i, j, L, W, edges)])
print(ret)