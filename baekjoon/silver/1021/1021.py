# input
# 10 10
# 1 6 3 2 7 9 8 4 10 5
# output
# 14
from collections import deque

n, m = map(int, input().split())
t = list(reversed(list(map(lambda x: int(x) - 1, input().split()))))
ans = 0
dq = deque([i for i in range(n)])
for i in range(m):
  target = t.pop()
  for j in range(len(dq)):
    if dq[j] == target:
      fa, fp, v = dq.append, dq.popleft, j
      break
    elif dq[-j] == target:
      fa, fp, v = dq.appendleft, dq.pop, j
      break
  for k in range(v):
    fa(fp())
  dq.popleft()
  ans += v
print(ans)
