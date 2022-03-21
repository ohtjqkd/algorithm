# 계단오르기
# dp정의 -> dp[i][j] -> i 계단으로 j + 1스탭 이동했을 때 최대값?
import sys

input = sys.stdin.readline

N = int(input())
score = [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]
dp[0][0], dp[1][1] = score[0], score[1]
dp[0][1] = score[0]
for i in range(N):
    if i + 1 < N:
        dp[i + 1][0] = max(dp[i + 1][0], score[i + 1] + dp[i][1]) # 3칸 연속 밟을 수 없기 때문에 dp[i][0]는 고려하지 않는다.
    if i + 2 < N:
        dp[i + 2][1] = max(dp[i + 2][1], score[i + 2] + max(dp[i]))
print(max(dp[N-1]))
