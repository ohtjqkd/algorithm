# input
# 3 3
# 1 1 0
# 1 1 1
# 1 0 1
# 1 1 1
# output
# 1

N, M = map(int, input().split(" "))
r, c, d = map(int, input().split(" "))

# d => 0: N, 1: E, 2: S, 3: W

area = [list(map(int, input().split(" "))) for _ in range(N)]

def check_rotate(r, c, d):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for i in range(4):
        d = (d + i) % 4
        xx, yy = r + dx[d], c + dy[d]
        if 0 <= xx < N and 0 <= yy < M and area[xx][yy] == 0:
            return d
        
while check(r, c, d):
