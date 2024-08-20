# input
# 4
# 3 5 2 7
# output
# 5 7 7 -1

N = int(input())

A = list(map(int, input().split(" ")))

result = [-1 for _ in range(N)]

stack = []

for i in range(N):
    if i == 0:
        stack.append((A[i], i))
        continue
    if stack:
        while stack:
            value, idx = stack[-1]
            if value < A[i]:
                result[idx] = A[i]
                stack.pop()
            else:
                break
        stack.append((A[i], i))
    if i == N-1:
        result[i] = -1
        continue

for ret in result:
    print(ret, end=" ")
