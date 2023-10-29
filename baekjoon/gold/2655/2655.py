# input
# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2
# output
# 3
# 5
# 3
# 1

N = int(input())

info = []
info_dict = dict()
for i in range(N):
  a, h, w = map(int, input().split())
  info.append((i, a, h, w))

dp = [[info[i][2], [info[i][0]]] for i in range(N)]
info.sort(key=lambda x: x[3])
for i in range(len(info) - 1):
  idx, a, h, w = info[i]
  for j in range(i + 1, len(info)):
    jdx, b, hh, ww = info[j]
    if info[i][1] > info[j][1] or info[i][3] > info[j][3]:
      continue
    if dp[jdx][0] < dp[idx][0] + hh:
      dp[jdx][0] = dp[idx][0] + hh
      dp[jdx][1] = dp[idx][1] + [jdx]
ret = max(dp, key=lambda x: x[0])
print(len(ret[1]))
for i in ret[1]:
  print(i+1)
  
