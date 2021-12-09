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
for i in range(T):
    num = list(input())
    for i in range(len(num)-1, 0, -1):
        if num[i] > num[i-1]:
            break
    else:
        print("BIGGEST")
        break
    s = sorted(num[i:], key=lambda x: (abs(int(x)-int(num[i-1])), -int(x)))
    ret = num[:i]+s
    ret[i], ret[i-1] = ret[i-1], ret[i]
    print(''.join(ret))

    