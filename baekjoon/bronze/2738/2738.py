# input
# 3 3
# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100
# output
# 4 4 4
# 6 6 6
# 5 6 100

N, M = map(int, input().split(" "))
A = [list(map(int, input().split(" "))) for _ in range(N)]
B = [list(map(int, input().split(" "))) for _ in range(N)]
for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]
for a in A:
    print(' '.join(map(str, a)))