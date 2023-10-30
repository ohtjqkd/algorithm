# input
# aabbbaa
# output
# 1
# FIXME
# pypy로 실행시 통과
from collections import Counter
S = list(input())
n = len(S)
c = Counter(S)
def dfs(prev, n):
    ret = 0
    if n == 0:
        return 1
    for k in c.keys():
        if k!=prev and c[k] !=0:
            c[k] -= 1
            ret += dfs(k, n-1)
            c[k] += 1
    return ret
print(dfs('', n))