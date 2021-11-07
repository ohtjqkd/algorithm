# input
# 5 1
# 5,6,3,9,-1

# output
# 1,-3,6,-10

N, K = tuple(map(int, input().split(" ")))
A = list(map(int, input().split(",")))
for _ in range(K):
    A = [A[i]-A[i-1] for i in range(1, len(A))]
print(','.join(list(map(str, A))))