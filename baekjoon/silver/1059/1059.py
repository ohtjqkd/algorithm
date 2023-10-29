# input
# 8
# 3 7 12 18 25 100 33 1000
# 59
# output
# 1065

l = int(input())
s = list(map(int, input().split()))
n = int(input())

mn, mx = 0, 1001
for a in s:
  if a == n:
    print(0)
    exit()
  if a < n and a > mn:
    mn = a
  elif a > n and a < mx:
    mx = a
print((n - mn) * (mx - n) - 1)
