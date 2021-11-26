# input: 6 3, 25 4, 2735 1
# output: 3, 0, 1

N, K = map(int, input().split(" "))
div = []
for i in range(1, N+1):
    if N % i == 0:
        K -= 1
    if K == 0:
        print(i)
        break
else:
    print(0)