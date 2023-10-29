# input
# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 3
# 2 3
# output
# 1 0 0 0 1 1 0 1

N = int(input())

s = list(map(int, input().split()))
m = int(input())

for _ in range(m):
  g, k = map(int, input().split())
  if g == 1:
    for i in range(k - 1, N, k):
      s[i] = s[i] ^ 1
  else:
    s[k - 1] = s[k - 1] ^ 1
    stack = []
    for i in range(min(N + 1 - k, k) - 1):
      if s[k - i - 2] == s[k + i]:
        s[k - i - 2] = s[k - i - 2] ^ 1
        s[k + i] = s[k + i] ^ 1
      else:
        break

for i in range(0, N, 20):
  print(' '.join(map(str, s[i : i + 20])))
