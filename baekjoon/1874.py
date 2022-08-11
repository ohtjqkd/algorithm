N = int(input())
target = []
for i in range(N):
    target.append(int(input()))

numbers = [i for i in range(N, 0, -1)]
stack = []
result = []
idx = 0
while numbers or stack:
    if stack and target[idx] == stack[-1]:
        stack.pop()
        result.append("-")
        idx += 1
    else:
        if not numbers:
            result = ["NO"]
            break
        n = numbers.pop()
        stack.append(n)
        result.append("+")

for i in result:
    print(i)


# from collections import deque

# N = int(input())
# target = deque([])
# for i in range(N):
#     target.appendleft(int(input()))
# stack, result = [], []

# for i in range(1, N + 1):
#     stack.append(i)
#     result.append("+")
#     while stack and stack[-1] == target[-1]:
#         stack.pop(), target.pop()
#         result.append("-")
# if len(target) > 0:
#     print("NO")
# else:
#     for sign in result:
#         print(sign)