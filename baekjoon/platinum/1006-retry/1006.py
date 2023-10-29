# input
# 1
# 8 100
# 70 60 55 43 57 60 44 50
# 58 40 47 90 45 52 80 40
# output
# 11

import sys
input = sys.stdin.readline

T = int(input())
n, s = map(int, input().split())

enemy = [list(map(int, input().split())) for _ in range(2)]

print(enemy)

# dp[i][j][0] = i, j의 위치에서 한 구역만 담당했을 때
# dp[i][j][1] = i, j의 위치에서 우측 구역을 담당했을 때
# dp[i][j][2] = i, j의 위체어서 위나 아래 구역을 담당했을 때
# 만약 불가능한 경우라면 inf를 입력
# dp[i][j][0] = dp[i][j]
dp = [[[float('inf')] * 3 for _ in range(n)] for _ in range(2)]
dp[0][0][0], dp[1][0][0] = 1, 1
if enemy[0][0] + enemy[0][1] <= s:
  dp[0][0][1] = 1
if enemy[1][0] + enemy[1][1] <= s:
  dp[1][0][1] = 1

for j in range(n):
  dp[0][j][0] = max(dp[0][j - 1][0], dp[0][j - 1][2], dp[1][j - 1][0], dp[1][j - 1][1], dp[1][j - 1][2]) + 1
  dp[0][j][1] = max(dp[0])
  dp[i][1][0] = 1
    
dp[0][j][0] = dp[0][j - 1][1] 을 제외한 j - 1 항 중에 max

# for i in range(n):
#   for j in range(2):
#     if dp[i][j]
    