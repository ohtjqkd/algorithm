# input
# 12
# 77
# 38
# 41
# 53
# 92
# 85
# output
# 256
# 41
sum = 0
min = float('inf')
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        sum += n
        if min > n:
            min = n
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)