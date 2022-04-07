# 가운데서 만나기
# prim? 아니넹
# 시간초과
import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
c2c = [[float('inf')] * N for _ in range(N)]
edges = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split(" "))
    edges[a-1].append((b-1, t))
    c2c[a-1][b-1] = t

min_cost = float('inf')
result = []
K = int(input())
start = list(map(lambda x: x-1, map(int, input().split(" "))))

for s in range(N):
    c2c[s][s] = 0
    stack = [s]
    while stack:
        now = stack.pop()
        for c, w in edges[now]:
            if c2c[s][now] + w < c2c[s][c]:
                c2c[s][c] = c2c[s][now] + w
                stack.append(c)

# ------- mingue's code ------- #
for i in range(N):
    for j in range(N):
        if i == j:
            c2c[i][j] = 0
            continue
        for k in range(N):
            c2c[j][k] = min(c2c[j][k], c2c[j][i] + c2c[i][k])
# ------------------------------ #
def max_weight(city, start):
    MAX = 0
    for s in start:
        if c2c[city][s] != float('inf') and c2c[s][city] != float('inf'):
            MAX = max(MAX, c2c[city][s] + c2c[s][city])
        else:
            return 0
    return MAX

for c in range(N):
    cost = max_weight(c, start)
    if cost == 0:
        continue
    if cost < min_cost:
        min_cost = cost
        result = [c+1]
    elif cost == min_cost:
        result.append(c+1)
print(' '.join(map(str, sorted(result))))