m = int(input())
n = list(map(int, input().split()))
count = len(n)
for i in n:
    if i == 1:
        count -= 1
        continue
    for j in range(2, i):
        if i % j == 0:
            count -= 1
            break
print(count)
