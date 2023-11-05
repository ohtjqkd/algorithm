# input
# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14
# output
# 4
import sys
input = sys.stdin.readline
N = int(input())
last_time, ret = 0, 0
times = []
for _ in range(N):
    start_time, end_time = map(int, input().split(" "))
    times.append([start_time, end_time])
times.sort(key=lambda x: (x[1], x[0]))
for t in times:
    if t[0] >= last_time:
        ret += 1
        last_time = t[1]
print(ret)
# 잘 이해가 안됨...