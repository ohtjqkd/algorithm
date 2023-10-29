# input
# 25 7 5
# output
# 2

a, b, n = map(int, input().split())

k = a % b

for i in range(n):
  k *= 10
  ans = k // b
  k %= b
print(ans)