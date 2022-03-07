from itertools import combinations
from collections import deque

answer = 0

N, M = map(int, input().split(" "))
map_ = [list(map(int, input().split(" "))) for _ in range(N)]
virus_loc = []
empty = []
for i in range(N):
    for j in range(M):
        if map_[i][j] == 0:
            empty.append((i, j))
        elif map_[i][j] == 2:
            virus_loc.append((i, j))
            
cand = list(combinations(empty, 3))

def count_safe(cand, virus, empty):
    for x, y in cand:
        map_[x][y] = 1
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    ret = len(empty) - 3
    visited = [[0 for _ in range(M)] for _ in range(N)]
    virus = deque(virus_loc)
    while virus:
        x, y = virus.popleft()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < N and 0 <= yy < M and map_[xx][yy] == 0 and visited[xx][yy] == 0:
                virus.append((xx, yy))
                visited[xx][yy] = 1
                ret -= 1
    for x, y in cand:
        map_[x][y] = 0
    return ret

for c in cand:
    answer = max(answer, count_safe(c, virus_loc, empty))
print(answer)

