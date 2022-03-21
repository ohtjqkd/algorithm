# 게임개발

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    N = int(input())
    D = []

    edges = [[] for _ in range(N + 1)] 
    indegree = [0] * (N + 1)
    cost = [0] * (N + 1)
    for n in range(N):
        arr = list(map(int, input().split(" ")))
        for p in arr[1:-1]:
            indegree[n + 1] += 1
            edges[p].append(n + 1)
        D.append(arr[0])
        cost[n + 1] = arr[0]
    q = deque([i for i in range(1, N + 1) if indegree[i] == 0])
    while q:
        curr = q.popleft()
        children = edges[curr]
        for c in children:
            indegree[c] -= 1
            if indegree[c] == 0:
                q.append(c)
            cost[c] = max(cost[c], cost[curr] + D[c - 1])
    return cost

for w in bfs()[1:]:
    print(w)