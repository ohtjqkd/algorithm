# input
# 8 9 5
# 1 8
# 3 10
# 4 5
# 5 20
# 7 12
# 8 15
# 9 50
# 14 14
# output
# 580

N, L, K = map(int, input().split())

difficuties = [list(map(int, input().split())) for _ in range(N)]

scores = []
for d in difficuties:
  if d[0] > L:
    scores.append(0)
  elif d[0] <= L < d[1]:
    scores.append(100)
  else:
    scores.append(140)
scores.sort(reverse=True)
print(sum(scores[:K]))
