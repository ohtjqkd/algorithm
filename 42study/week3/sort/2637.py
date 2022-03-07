# 장난감 조립

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
visited = [0] * N
indeg = [0] * N
weight = [[0] * N for _ in range(N)]
cost = [[0] * N for _ in range(N)]
edges = [[] for _ in range(N)]
for _ in range(M):
    x, y, k = list(map(int, input().split(" ")))
    edges[y-1].append(x-1)
    indeg[x-1] += 1
    weight[y-1][x-1] = k
base_part,q = [], []
for i in range(N):
    if indeg[i] == 0:
        base_part.append(i)
        q.append(i)
for i in base_part:
    cost[i][i] = 1
while q:
    curr = q.pop()
    C = cost[curr]
    for c in edges[curr]:
        indeg[c] -= 1
        if indeg[c] == 0:
            q.append(c)
        for i, v in enumerate(C):
            cost[c][i] += v * weight[curr][c]
for b in base_part:
    print(b+1, cost[N-1][b])
