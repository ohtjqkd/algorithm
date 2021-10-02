n = int(input())
dp = [[0]*12 for _ in range(n)]
for i in range(1, 11):
    dp[0][i] = 1
for j in range(1, n):
    for i in range(1, 11):
        dp[j][i] = dp[j-1][i-1] + dp[j-1][i+1]
result = 0
for i in range(2, 11):
    result += dp[n-1][i]

print(result % (1000000000))
