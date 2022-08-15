# input
# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1
# output
# 7

from collections import deque

gears = [deque(list(input())) for _ in range(4)]

K = int(input())

def rotate(gear: deque, dir: int):
    if dir == -1:
        gear.append(gear.popleft())
    else:
        gear.appendleft(gear.pop())
    return gear

for _ in range(K):
    start, dir = map(int, input().split(" "))
    start -= 1
    move_com = [(start, dir)]
    tmp_dir = dir
    for i in range(start - 1, -1, -1):
        if gears[i][2] == gears[i + 1][-2]:
            break
        tmp_dir = -tmp_dir
        move_com.append((i, tmp_dir))
    tmp_dir = dir
    for i in range(start + 1, 4):
        if gears[i - 1][2] == gears[i][-2]:
            break
        tmp_dir = -tmp_dir
        move_com.append((i, tmp_dir))
    for i, dir in move_com:
        gears[i] = rotate(gears[i], dir)
ret = 0
for i, g in enumerate(gears):
    if g[0] == '1':
        ret += (2 ** i)
print(ret)