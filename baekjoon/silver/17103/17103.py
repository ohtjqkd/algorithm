# input
# 5
# 6
# 8
# 10
# 12
# 100
# output
# 1
# 1
# 2
# 1
# 6

# 2 < n <= 1,000,000

# 1. 소수를 구한다.
# 2. 소수의 합이 n이 되는 경우의 수를 구한다.
# 3. 소수의 합이 n이 되는 경우의 수를 출력한다.

is_prime = [1 for _ in range(1000001)]
is_prime[0], is_prime[1] = 0, 0
prime = []
prime_set = set()
for i in range(2, 1000001):
  if is_prime[i] == 1:
    prime.append(i)
    prime_set.add(i)
    mul = 1
    while i * mul <= 1000000:
      is_prime[i * mul] = 0
      mul += 1

gold_cnt = [0 for _ in range(1000001)]

T = int(input())

for i in range(T):
  n = int(input())
  cnt = 0
  for p in prime:
    if prime_set.__contains__(n - p) and p <= n - p:
      cnt += 1
  print(cnt)