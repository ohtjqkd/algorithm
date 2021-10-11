#input
#3 2 3
# print((sum(arr)+3)//2)

arr = list(map(int, input().split()))

sums = [0 for _ in range(sum(arr)+1)]

for i in range(1, arr[0]+1):
    for j in range(1, arr[1]+1):
        for k in range(1, arr[2]+1):
            sums[i+j+k] += 1
print(sums)
max_sum = max(sums)
for i, s in enumerate(sums):
    if s == max_sum:
        print(i)
        break