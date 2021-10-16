# input
# aabbbaa
# output
# 1

from collections import Counter
S = list(input())
n = len(S)
c = Counter(S)

def comb(prev, c, n):
    ret = 0
    if n == 0:
        return 1
    for k in c.keys():
        if k == prev or c[k] == 0:
            continue
        print(k)
        c[k] -= 1
        ret += comb(k, c, n-1)
        c[k] += 1
    return ret
ret = comb(None, c, n)
print(ret)
