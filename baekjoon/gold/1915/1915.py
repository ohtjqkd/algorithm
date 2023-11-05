n, m = map(int, input().split(" "))
# arr = list(map(int, input()))
board = [list(map(int, input())) for _ in range(n)]

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
max_side = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
            max_side = max(max_side, dp[i+1][j+1])

print(max_side ** 2)
