# input
# 6 2
# 3 3 3 3 3 3
# 2 3 3 3 3 3
# 2 2 2 3 2 3
# 1 1 1 2 2 2
# 1 1 1 3 3 1
# 1 1 2 3 3 2
# output
# 3

from collections import deque

N, L = map(int, input().split(" "))

board = [list(map(int, input().split(" "))) for _ in range(N)]
ret = 0

def check_row(r, L):
    left_dp = [1 for _ in range(N)]
    right_dp = [1 for _ in range(N)]

    for i in range(1, N):
        if board[r][i] == board[r][i - 1]:
            left_dp[i] += left_dp[i - 1]
        if board[r][-i] == board[r][-(i + 1)]:
            right_dp[-(i + 1)] += right_dp[-i]
    for i in range(1, N):
        if board[r][i] > board[r][i - 1]:
            if left_dp[i - 1] < L:
                return 0
        elif board[r][i] < board[r][i - 1]:
            if right_dp[i] < L:
                return 0
    return 1

def check_col(c, L):
    up_dp = [1 for _ in range(N)]
    down_dp = [1 for _ in range(N)]
    for i in range(1, N):
        if board[i][c] == board[i - 1][c]:
            up_dp[i] += up_dp[i - 1]
        if board[-i][c] == board[-(i + 1)][c]:
            down_dp[-(i + 1)] += down_dp[-i]
    for i in range(1, N):
        if board[i][c] == board[i - 1][c]:
            up_dp[i] += up_dp[i - 1]
        if board[-i][c] == board[-(i + 1)][c]:
            down_dp[-(i + 1)] += down_dp[-i]
    for i in range(1, N):
        if board[i][c] > board[i - 1][c]:
            if up_dp[i - 1] < L:
                return 0
            else:
                for j in range(L):
                    
        elif board[i][c] < board[i - 1][c]:
            if down_dp[i] < L:
                return 0
    return 1

for i in range(N):
    ret += check_row(i, L)
    ret += check_col(i, L)
    print(ret)
print(ret)