n, k = map(int, input().split())
pack = []
dp = [0] * 100001
for _ in range(n):
    pack.append(list(map(int, input().split())))

for i in range(len(pack)):
    w, v = pack[i]
    for j in range(k, w-1, -1):
        if w <= k:
            dp[j] = max(dp[j], dp[j-w] + v)

print(max(dp))
