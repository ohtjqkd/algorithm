# 곡예비행
import sys
print(-sys.maxsize - 1)
N, M = map(int, input().split(" "))

score_board = [list(map(int, input().split(" "))) for _ in range(N)]

up_dp = [[0] * M for _ in range(N)]
down_dp = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        up_dp[i][j], down_dp[i][j] = score_board[i][j], score_board[i][j]

for i in range(N - 2, -1, -1):
    up_dp[i][0] += up_dp[i + 1][0]
    down_dp[i][M - 1] += down_dp[i + 1][M - 1]
for i in range(1, M):
    up_dp[N - 1][i] += up_dp[N - 1][i - 1]
    down_dp[N - 1][M - i - 1] += down_dp[N - 1][M - i]
for i in range(N - 2, -1, -1):
    for j in range(1, M):
        up_dp[i][j] += max(up_dp[i + 1][j], up_dp[i][j - 1])
        down_dp[i][M - j - 1] += max(down_dp[i + 1][M - j - 1], down_dp[i][M - j])

ret = float("-inf")

for j in range(M):
    ret = max(ret, up_dp[0][j] + down_dp[0][j])

print(ret)