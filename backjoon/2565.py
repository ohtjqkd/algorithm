n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))
dp = [1] * n

lines.sort()

for i in range(n):
    for j in range(i-1, -1, -1):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))
