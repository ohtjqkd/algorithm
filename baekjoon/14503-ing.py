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
ret = 0

def check_rotate(r, c, d):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for i in range(3, -1, -1):
        dd = (d + i) % 4
        xx, yy = r + dx[dd], c + dy[dd]
        if 1 <= xx < N - 1 and 1 <= yy < M - 1 and area[xx][yy] == 0:
            return [True, xx, yy, dd]
    else:
        return [False, r - dx[d], c - dy[d], d]
        
while True:
    if area[r][c] ==  0:
        ret += 1
    area[r][c] = 2
    is_avail, r, c, d = check_rotate(r, c, d)
    if is_avail:
        pass
    elif area[r][c] == 1:
        break
print(ret)
