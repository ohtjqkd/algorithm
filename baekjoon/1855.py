# input
# 3
# aeijfbcgklhd
# output
# abcdefghijkl
import math

col = int(input())
norm = list(input())
row = int(math.ceil(len(norm)/col))
ret = []
for i in range(col):
    for j in range(row):
        idx = j * col + i if j % 2 == 0 else (j+1) * col - (i+1)
        ret.append(norm[idx])
print(''.join(ret))
