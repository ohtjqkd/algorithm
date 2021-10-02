k = int(input())
arr = []
sums = 0
for _ in range(k):
    n = int(input())
    if n == 0:
        sums -= arr.pop()
    else:
        arr.append(n)
        sums += n

print(sums)
