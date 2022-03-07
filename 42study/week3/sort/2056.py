# 작업

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

edges = [[] for _ in range(N)]
weight = [0] * N
cost = [0] * N
indegree = [0] * N
for i in range(N):
    arr = list(map(int, input().split(" ")))
    weight[i], cost[i] = arr[0], arr[0]
    for p in arr[2:]:
        if p - 1 > i:
            continue
        edges[p-1].append(i)
        indegree[i] += 1
q = deque([i for i in range(N) if indegree[i] == 0])
while q:
    curr = q.popleft()
    for c in edges[curr]:
        indegree[c] -= 1
        if indegree[c] == 0:
            q.append(c)
        cost[c] = max(cost[c], cost[curr] + weight[c])
print(max(cost))