# 줄 세우기

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))
ret = []
indeg = [0] * N
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split(" "))
    edges[a-1].append(b-1)
    indeg[b-1] += 1

## 깊이 우선 탐색도 가능하다!

# q = deque([i for i, v in enumerate(indeg) if v == 0])
q = [i for i, v in enumerate(indeg) if v == 0]
while q:
    # curr = q.popleft()
    curr = q.pop()
    ret.append(curr+1)
    for c in edges[curr]:
        indeg[c] -= 1
        if indeg[c] == 0:
            q.append(c)
print(ret)