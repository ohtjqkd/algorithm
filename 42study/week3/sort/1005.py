# ACM Craft

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def bfs():
    N, K = map(int, input().split(" "))
    D = list(map(int, input().split(" ")))

    edges = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    weight = [0  if i == 0 else D[i - 1] for i in range(N + 1)]
    for _ in range(K):
        x, y = map(int, input().split(" "))
        indegree[y] += 1
        edges[x].append(y)
    W = int(input())
    q = deque([i for i in range(1, N + 1) if indegree[i] == 0])
    while q:
        curr = q.popleft()
        children = edges[curr]
        for c in children:
            indegree[c] -= 1
            if indegree[c] == 0:
                q.append(c)
            weight[c] = max(weight[c], weight[curr] + D[c - 1])
            print(indegree)
    return weight[W]


for _ in range(T):
    print(bfs())