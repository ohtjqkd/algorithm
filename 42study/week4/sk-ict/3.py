# 3번 문제

# 각 diag까지의 경우의 수 * 그 diag에서 도착점까지의 경우의 수

def solution(width, height, diagonals):
    W, H = width+1, height+1
    path = [[0 if i != 0 and j != 0 else 1 for i in range(W)] for j in range(H)]
    ret = 0
    for i in range(1, H):
        for j in range(1, W):
            path[i][j] = (path[i - 1][j] + path[i][j - 1]) % 10000019
    for y, x in diagonals:
        ret += (path[x][y - 1] * path[H - x][W - y - 1] + path[x - 1][y] * path[H - x - 1][W - y])
    print(ret % 10000019)
solution(51, 37, [[17,19]])
solution(2, 2, [[1,1],[2,2]])
