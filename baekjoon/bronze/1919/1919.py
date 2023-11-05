# input
# aabbcc
# xxyybb
# output
# 8
from collections import defaultdict

A, B = input(), input()
a_dict, b_dict = defaultdict(int), defaultdict(int)
alph = set()
ret = 0
for a in A:
    alph.add(a)
    a_dict[a] += 1
for b in B:
    alph.add(b)
    b_dict[b] += 1
for a in alph:
    ret += abs(a_dict[a]-b_dict[a])
print(ret)