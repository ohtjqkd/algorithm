# input
# 0 1 0 1
# 1 1 1 0
# 0 0 1 1
# output
# B
# A
# B
from collections import Counter
p = "EABCD"
yuts = [Counter(list(map(int, input().split(" ")))) for _ in range(3)]
for y in yuts:
    print(y)
    print(p[y.get(0, 0)])
