# input
# 5 4
# 0 0 1 0 2
# 2 3 2 1 0
# 4 3 2 9 0
# 1 0 2 9 0
# 8 8 2 1 0
# 1 3
# 3 4
# 8 1
# 4 8
# output
# 77

N, M = map(int, input().split(" "))
MAP = [list(map(int, input().split(' '))) for _ in range(N)]
dx, dy = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]
cloud = set([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])
def make_cloud(m, before_cloud):
    c = set()
    for i in range(N):
        for j in range(N):
            if m[i][j] >= 2 and (i, j) not in before_cloud:
                c.add((i, j))
                m[i][j] -= 2
    return [c, m]

def move_cloud(cloud, dir, weight):
    moved = set()
    for r, c, in cloud:
        xx = (N + (r + weight * dx[dir]) % N) % N
        yy = (N + (c + weight * dy[dir]) % N) % N
        moved.add((xx, yy))
    return moved

def add_water(cloud, m):
    for r, c in cloud:
        m[r][c] += 1
    return m

def dup_water(cloud, m):
    for r, c in cloud:
        dup_cnt = 0
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            rr, cc = r + dr, c + dc
            if 0 <= rr < N and 0 <= cc < N:
                if m[rr][cc] > 0:
                    dup_cnt += 1
        m[r][c] += dup_cnt
    return m

for _ in range(M):
    dir, weight = map(int, input().split(" "))
    moved_cloud = move_cloud(cloud, dir, weight)
    MAP = add_water(moved_cloud, MAP)
    MAP = dup_water(moved_cloud, MAP)
    cloud, MAP = make_cloud(MAP, moved_cloud)

SUM = 0
for i in MAP:
    for j in i:
        SUM += j
print(SUM)