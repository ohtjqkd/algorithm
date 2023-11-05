# input
# 60
# 100
# output
# 245
# 64
from math import sqrt, ceil

M, N = int(input()), int(input())
ret = 0
m, n = ceil(sqrt(M)), ceil(sqrt(N))
li = []
for i in range(m, n+1):
    if M<= i**2 <=N:
        li.append(i**2)
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(li[0])