n = int(input())

dp = [10**6] * (n+1)

dp[1] = 0

for i in range(n+1):
    if i+1 <= n:
        dp[i+1] = min(dp[i]+1, dp[i+1])
    if i*3 <= n:
        dp[i*3] = min(dp[i]+1, dp[i*3])
    if i*2 <= n:
        dp[i*2] = min(dp[i]+1, dp[i*2])

print(dp[n])

# second

X = int(input())

dp = [0 for _ in range(X+1)]

for i in range(2, len(dp)):
    m = dp[i-1]
    t = dp[i//2] if i % 2 == 0 else float('inf')
    th = dp[i//3] if i % 3 == 0 else float('inf')
    dp[i] = min(m, t, th)+1
print(dp)

# input

# 2