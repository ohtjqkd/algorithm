# input
# 2 20 50
# 50 30
# 20 40
# output
# 1
from collections import deque
N, L, R = map(int, input().split(" "))
# for _ in range(N):
#     print(input().split(" "))
country = [list(map(int, input().split(" "))) for _ in range(N)]

def dfs(country, visited, x, y, L, R):
    ret = 0
    deq = deque([(x, y)])
    visited[x][y] = 1
    sector = []
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    while deq:
        r, c = deq.popleft()
        sector.append((r, c))
        curr = country[r][c]
        ret += curr
        for i in range(4):
            xx, yy = r + dx[i], c + dy[i]
            if 0 <= xx < N and 0 <= yy < N and visited[xx][yy] == 0 and L <= abs(curr - country[xx][yy]) <= R:
                deq.append((xx, yy))
                visited[xx][yy] = 1
            
    return [ret, sector, visited]
k = 0
while True:
    flag = False
    sectors = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            s, section, visited = dfs(country, visited, i, j, L, R)
            if len(section) > 1:
                sectors.append([s, section])
                flag = True
    if not flag:
        print(k)
        break
    for s, sector in sectors:
        for r, c in sector:
            country[r][c] = s // len(sector)
    k += 1