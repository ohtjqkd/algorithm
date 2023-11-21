n = int(input())

arr = list(map(int, input().split()))
dp = [0] * n
for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            dp[j] = max(dp[i]+1, dp[j])
dp1 = [0] * n
for i in range(n-1):
    for j in range(i+1, n):
        if arr[-i-1] < arr[-j-1]:
            dp1[-j-1] = max(dp1[-i-1]+1, dp1[-j-1])
print(dp, dp1)
result = [dp[i]+dp1[i] for i in range(n)]
print(max(result)+1)
