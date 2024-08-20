# input
# 3
# 4
# 7
# 10
for _ in range(int(input())):
    n = int(input())
    dp = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        dp[i] += dp[i-2]
        
    for i in range(3, n+1):
        dp[i] += dp[i-3]
    print(dp[-1])
