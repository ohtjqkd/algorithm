N, M = map(int, input().split(" "))

if N < M:
    N, M = M, N

div = N // M + 1
mode = N % M

print(div * M + mode)
