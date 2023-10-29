# input
# 1000000000 2
# output
# 199999998 199999999 200000000 200000001 200000002

def solution():
  n, k = map(int, input().split())
  while k <= 100:
    for i in range(int(n / k - k), int(n / k + k)):
      if i < 0:
        continue
      if k * (2 * i + (k - 1)) / 2 == float(n):
        return i, k
    k += 1
  return -1, 1
    
s, k = solution()
ans = [str(i) for i in range(s, s + k)]
print(' '.join(ans))

