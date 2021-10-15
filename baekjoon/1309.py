# input
# 4

n = int(input())

dp = [0 for _ in range(n+1)]
dp[0], dp[1] = 1, 3

for i in range(2, n+1):
    dp[i] = (dp[i-2]*3+(dp[i-1]-dp[i-2]) * 2)%9901
print(dp[n])