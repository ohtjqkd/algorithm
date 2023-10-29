from heapq import heappop, heappush

S = input()
M = int(input())
score_dict = dict()

for i in range(M):
  q = input().split(' ')
  score_dict[q[0]] = int(q[1])

dp = [0 for i in range(len(S))]

for i in range(len(S)):
  for j in range(i, -1, -1):
    s = S[j : i + 1]
    if j == 0:
      dp[i] = max(dp[i], score_dict.get(s, len(s)))
    else:
      dp[i] = max(dp[i], score_dict.get(s, len(s)) + dp[j - 1])
print(dp[-1])
