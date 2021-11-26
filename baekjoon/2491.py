# input
# 9
# 1 2 2 4 4 5 7 7 2
# output: 8
N = int(input())
li = list(map(int, input().split(" ")))
ret = 1
asc, desc = 1, 1
for i in range(1, len(li)):
    if li[i] > li[i-1]:
        asc += 1
        desc = 1
    elif li[i] < li[i-1]:
        desc += 1
        asc = 1
    else:
        asc += 1
        desc += 1
    ret = max([ret, desc, asc])
print(ret)
