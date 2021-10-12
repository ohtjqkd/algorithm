import math
m, n = map(int, input().split())
prime_n = [0] * (n+1)
prime_n[1], prime_n[0] = 1, 1
for i in range(2, int(math.sqrt(n))+1):
    for j in range(2, n//i+1):
        prime_n[i*j] = 1

for idx, i in enumerate(prime_n):
    if i == 0 and m <= idx and idx <= n:
        print(idx)
