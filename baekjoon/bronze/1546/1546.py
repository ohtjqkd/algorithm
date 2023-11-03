n = int(input())
s = list(map(int, input().split()))

max_v = 0
for i in s:
    if i > max_v:
        max_v = i
sum = 0
for i in s:
    sum += i/max_v*100
print(sum/n)
