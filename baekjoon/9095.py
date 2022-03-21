# input
# 3
# 4
# 7
# 10
# output
# 7
# 44
# 274

for _ in range(int(input())):
    n = int(input())
    dp = [0 for _ in range(n-1)]
    dp[0:2] = [1, 1, 1]
    for i in range(len(dp)):
        if i + 1 < len(dp):
            dp[i+1] = dp[i] + dp[i+1]
        if i + 2 < len(dp): 
            dp[i+2] = dp[i] + dp[i+2]
        if i + 3 < len(dp): 
            dp[i+3] = dp[i] + dp[i+3]
    print(dp)
    print(dp[-1])

