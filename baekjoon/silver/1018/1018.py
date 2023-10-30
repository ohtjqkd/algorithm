# input
# 11 12
# BWWBWWBWWBWW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# BWWBWBWWWBWW
# WBWWBWBBWWBW
# BWWBWBBWWBWW
# WBWWBWBBWWBW
# output
# 15

n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = n*m


def start_white(x, y):
    result = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i-x+j-y) % 2 == 0 and board[i][j] == 'B':
                result += 1
            elif (i-x+j-y) % 2 == 1 and board[i][j] == 'W':
                result += 1
    return result


def start_black(x, y):
    result = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i-x+j-y) % 2 == 0 and board[i][j] == 'W':
                result += 1
            elif (i-x+j-y) % 2 == 1 and board[i][j] == 'B':
                result += 1
    return result


for i in range(0, n-7):
    for j in range(0, m-7):
        result = min(result, start_white(i, j))
        result = min(result, start_black(i, j))

print(result)
