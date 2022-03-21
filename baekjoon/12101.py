n, k = map(int, input().split(" "))


stack = [[[1], 1]]
while stack:
    li, s = stack.pop()
    if s == n and k == 0:
        print('+'.join(li))
    for i in range(3, 0, -1):
        stack.append()

