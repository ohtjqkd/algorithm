n = int(input())
init = n
i = 0

while True:
    left_num, right_num = init//10, init % 10
    sum_num = left_num+right_num
    if sum_num >= 10:
        sum_num %= 10
    init = right_num * 10 + sum_num
    i += 1
    if init == n:
        break

print(i)
