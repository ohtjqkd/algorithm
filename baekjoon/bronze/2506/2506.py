# input
# 10
# 1 0 1 1 1 0 0 1 1 0
# output: 10

N = int(input())
score = list(map(int, input().split(" ")))
dp = [0 for _ in range(len(score))]
dp[0] = score[0]
for i in range(1, len(dp)):
    if score[i] == 1:
        dp[i] = dp[i-1] + score[i]
    else:
        dp[i] = score[i]
print(sum(dp))