# 작업

# 위상정렬인줄 알았지만 아니다
import sys

input = sys.stdin.readline
N, M = map(int, input().split(" "))
edges = [[] for _ in range(N)]
visited = [0] * N
for _ in range(M):
    a, b = map(int, input().split(" "))
    edges[b-1].append(a-1)

result = 0
stack = [int(input()) - 1]

while stack:
    now = stack.pop()
    for nxt in edges[now]:
        if visited[nxt]:
            continue
        result += 1
        visited[nxt] = 1
        stack.append(nxt)
print(result)