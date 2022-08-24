# input
# 2 20 50
# 50 30
# 20 40
# output
# 1
N, L, R = map(int, input().split(" "))

country = [list(map(int, input().split(" "))) for _ in range(N)]

def dfs(country, visited, x, y, L, R):
    ret = 0
    stack = [(x, y)]
    sector = []
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    while stack:
        print(stack)
        r, c = stack.pop()
        sector.append((r, c))
        visited[r][c] = 1
        curr = country[r][c]
        ret += curr
        for i in range(4):
            xx, yy = r + dx[i], c + dy[i]
            if 0 <= xx < N and 0 <= yy < N and visited[xx][yy] == 0 and L <= abs(curr - country[xx][yy]) <= R:
                stack.append((xx, yy))
                ret += r
            
    return [ret, sector, visited]

for k in range(2001):
    flag = False
    sectors = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            s, section, visited = dfs(country, visited, i, j, L, R)
            if len(section) > 1:
                sectors.append([s, section])
                flag = True
    print(sectors)
    if not flag:
        print(k)
        break
    for s, sector in sectors:
        for r, c in sector:
            country[r][c] = s // len(sector)
print(country)