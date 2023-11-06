# input
# 2
# 6
# 24
# output
# 2 1
# 3 1
# 2 3
# 3 1
N = int(input())
answer_li = [0 for _ in range(100001)]
prime = []
for i in range(2, 100001):
    if answer_li[i] == 0:
        prime.append(i)
    for j in range(1, 100001//i+1):
        if i*j > 100000:
            break
        answer_li[i*j] = 1
for _ in range(N):
    n = int(input())
    for p in prime:
        cnt = 0
        if n == 1:
            break
        while n % p == 0:
            cnt += 1
            n //= p
        if cnt != 0:
            print(f'{p} {cnt}')