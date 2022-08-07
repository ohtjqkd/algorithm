# 구데기컵 문제 이건 내가 풀게 아니더라..

import sys
T = int(input())
i = 0
while i ** 2 < 1000000000:
    i += 1
prime = [0 for _ in range(i + 1)]
print(len(prime))
start = 2
# while start < len(prime):
