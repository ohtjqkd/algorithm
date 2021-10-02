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
