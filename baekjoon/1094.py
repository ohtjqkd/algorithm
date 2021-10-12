n = int(input())
ret = 0
for i in range(6, -1, -1):
    if n % (2**i) != n:
        ret += 1
        n %= (2**i)
print(ret)

# input
# 23