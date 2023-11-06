n = int(input())
result = 0
for i in range(n):
    tmp = i
    sum_tmp = i
    while tmp >= 1:
        sum_tmp += tmp % 10
        tmp //= 10
    if sum_tmp == n:
        result = i
        break
print(result)
