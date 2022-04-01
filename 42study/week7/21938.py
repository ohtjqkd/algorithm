# 영상처리

import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
pic = [list(map(int, input().split(" "))) for _ in range(N)]
new_pic = [[0] * M for _ in range(N)]
T = int(input()) * 3
result = 0

def calc_sum(i, j):
    return pic[i][j] + pic[i][j+1] + pic[i][j+2]

def dfs(i, j):
    stack = [(i, j)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if xx < 0 or xx >= N or yy < 0 or yy >= M:
                continue
            if new_pic[xx][yy] == 1:
                stack.append((xx, yy))
                new_pic[xx][yy] = 0

for i in range(N):
    for j in range(M):
        now_sum = calc_sum(i, 3*j)
        if now_sum == 0:
            continue
        if now_sum >= T:
            new_pic[i][j] = 1
        else:
            new_pic[i][j] = 0
for i in range(N):
    for j in range(M):
        if new_pic[i][j] == 1:
            dfs(i, j)
            result += 1
print(result)