# 블로그
from collections import deque
X, N = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
dp = [a for a in A]
M, ret = 0, 0
for i in range(1, len(A)):
    dp[i] += dp[i - 1]
for i in range(N - 1, len(A)):
    sub = dp[i] - dp[i - N]
    if i == N - 1:
        M = dp[i]
        ret = 1
    elif sub > M:
        M = sub
        ret = 1
    elif sub == M:
        ret += 1
if M != 0:
    print(M)
    print(ret)
else:
    print("SAD")