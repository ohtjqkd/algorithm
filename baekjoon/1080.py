N, M = map(int, input().split(" "))
init = [list(map(int, list(input()))) for _ in range(N)]
target = [list(map(int, list(input()))) for _ in range(N)]

cnt = 0
isAvailable = False


def reverse(x, y):
    global init
    for i in range(3):
        for j in range(3):
            init[x+i][y+j] ^= 1

for i in range(N-2):
    for j in range(M-2):
        if init == target:
            isAvailable = True
            break
        if init[i][j] != target[i][j]:
            reverse(i, j)
            cnt += 1
if isAvailable or init == target:
    print(cnt)
else:
    print(-1)
