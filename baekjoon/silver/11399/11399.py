# input
# 5
# 3 1 4 3 2
# output
# 32
N = int(input())
P = list(map(int, input().split(" ")))
P.sort()
for i in range(1, len(P)):
    P[i] += P[i-1]
for i in range(1, len(P)):
    P[i] += P[i-1]    
print(P[-1])