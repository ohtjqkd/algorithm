n = int(input())
values = list(map(int, input().split()))

# 완전탐색

min_v = 10000000
max_v = -10000000

for v in values:
    if min_v > v:
        min_v = v
    if max_v < v:
        max_v = v

# sorting을 이용한 풀이
# values.sort()
# min_v, max_v = values[0], values[-1]

print(min_v, max_v)
