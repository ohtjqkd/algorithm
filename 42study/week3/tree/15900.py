# 나무탈출

import sys

input = sys.stdin.readline
N = int(input())
answer = 0
visited = [0 for _ in range(N)]
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split(" "))
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
nodes = [(0, 0)]
while nodes:
    curr, depth = nodes.pop()
    is_leaf = True
    visited[curr] = 1
    children = edges[curr]
    for c in children:
        if visited[c] == 1:
            continue
        is_leaf = False
        nodes.append((c, depth + 1))
    if is_leaf:
        answer += depth
print(answer)
if answer % 2 == 1:
    print("YES")
else:
    print("NO")
