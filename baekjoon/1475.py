# input: 9999, 122, 12635, 888888
# output: 2, 2, 1, 6
from collections import Counter
import math

num = input()
cnt = [0 for _ in range(10)]
for s in num:
    cnt[int(s)] += 1
max_value = max([cnt[i] for i in range(10) if i != 6 and i != 9])
s_n = int(math.ceil((cnt[6] + cnt[9]) / 2))
ret = max_value if max_value > s_n else s_n
print(ret)
