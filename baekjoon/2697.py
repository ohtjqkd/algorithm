# input
# 3
# 123
# 279134399742
# 987
# output
# 132
# 279134423799
# BIGGEST

T = int(input())
for _ in range(T):
    num = list(input())
    is_biggest = True
    for i in range(len(num)-2, -1, -1):
        if num[i + 1] > num[i]:
            is_biggest = False
            break
    if is_biggest:
        print('BIGGEST')
    else:
        target = num[i]
        min_idx = i+1
        for j in range(i + 1, len(num)):
            if num[j] > target:
                if num[j] < num[min_idx]:
                    min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]
        num[i+1:].sort()
        num = num[:i + 1] + sorted(num[i + 1:])
        print(''.join(num))