import sys
sys.setrecursionlimit = 100000

def solution(img, x, y, rg = True):
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    RG = ['R', 'G']
    curr_color = img[x][y]
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        img[x][y] = 0
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < len(img) and 0 <= yy < len(img[0]) and img[xx][yy] != 0:
                if curr_color == img[xx][yy]:
                    stack.append((xx, yy))
                elif rg and curr_color in RG and img[xx][yy] in RG:
                    stack.append((xx, yy))
    # print(img)
    return 1

n = int(input())
img = [[],[]]
for i in range(n):
    row = list(input())
    img[0].append(row[::])
    img[1].append(row[::])
answer = [0, 0]
for i in range(n):
    for j in range(n):
        if img[0][i][j] != 0:
            answer[0] += solution(img[0], i, j, rg=False)
            # print(answer[0])
for i in range(n):
    for j in range(n):
        if img[1][i][j] != 0:
            answer[1] += solution(img[1], i, j, rg=True)
            # print(answer[1])
print(answer[0], answer[1])
