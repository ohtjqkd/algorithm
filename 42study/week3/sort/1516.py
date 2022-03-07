# 게임개발

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    N = int(input())
    D = []

    edges = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    weight = [0] * (N + 1)
    for n in range(N):
        arr = list(map(int, input().split(" ")))
        for p in arr[1:-1]:
            indegree[n + 1] += 1
            edges[p].append(n + 1)
        D.append(arr[0])
        weight[n + 1] = arr[0]
    q = deque([i for i in range(1, N + 1) if indegree[i] == 0])
    while q:
        curr = q.popleft()
        children = edges[curr]
        for c in children:
            indegree[c] -= 1
            if indegree[c] == 0:
                q.append(c)
            weight[c] = max(weight[c], weight[curr] + D[c - 1])
    return weight

for w in bfs()[1:]:
    print(w)