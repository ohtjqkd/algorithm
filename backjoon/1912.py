n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    if arr[i] > arr[i] + dp[i-1]:
        dp[i] = arr[i]
    else:
        dp[i] = arr[i]+dp[i-1]

print(max(dp))
