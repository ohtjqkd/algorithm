# input
# 4 11
# 802
# 743
# 457
# 539
# output
# 200
K, N = tuple(map(int, input().split(" ")))
lan = [int(input()) for _ in range(K)]
total = sum(lan)
left, right = 1, total//N
while left < right:
    S = 0
    mid = (left + right) // 2
    for l in lan:
        S += l//mid
    if S >= N:
        left = mid+1
    else:
        right = mid-1
S = 0
for l in lan:
    S += l//((left+right)//2)
if S < N:
    print((left+right)//2-1)
else:
    print((left+right)//2)