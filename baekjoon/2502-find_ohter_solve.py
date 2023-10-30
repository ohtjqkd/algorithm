# input: 6 41
# output
# 2
# 7

# 다시 생각해보기
import sys
D, K = map(int, input().split(" "))
dp = [0 for _ in range(D)]
for i in range(1, 100000+1):
    for j in range(i, 100000+1):
        dp[0], dp[1] = i, j
        for k in range(2, len(dp)):
            dp[k] = dp[k-1] + dp[k-2]
            if dp[k] > K or k > D:
                break
            if dp[k] == K and k+1 == D:
                print(i)
                print(j)
                sys.exit()
