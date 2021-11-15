# input: 3, 2000000
# output: 12, 3999999999999000000

N = int(input())
ret = 0
for i in range(1, N):
    ret += N*i+i
print(ret)