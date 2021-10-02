n = int(input())
q = [0] * 10000
dp = [[0, 0] for _ in range(10000)]
for i in range(n):
    q[i] = int(input())
dp[0][0], dp[1][0], dp[2][0] = q[0], q[0]+q[1], q[1]+q[2]
dp[0][1], dp[1][1], dp[2][1] = q[0], q[1], q[0]+q[2]
maxs = 0
for i in range(3, n):
    dp[i][0] = dp[i-1][1]+q[i]
    dp[i][1] = max(max(dp[i-3]), max(dp[i-2]))+q[i]
print(max(max(dp[n-1]), max(dp[n-2])))
