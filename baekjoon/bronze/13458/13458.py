# input
# 1
# 1
# 1 1
# output: 1

import math

N = int(input())
A = list(map(int, input().split(" ")))
B, C = map(int, input().split(" "))
answer = 0
for i in range(len(A)):
    answer += 1
    answer += math.ceil(max(A[i]-B, 0)/C)
print(answer)
