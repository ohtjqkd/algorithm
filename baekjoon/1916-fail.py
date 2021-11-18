# input
# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5
# output
# 4

# 최소경로를 구하는 문제이다
from collections import defaultdict
from heapq import heapify, heappop, heappush
import sys
lines = sys.stdin.read().split("\n")
# print(lines)
N = int(lines[0])
M = int(lines[1])
heap = []
maps = defaultdict(list)
fee = [float('inf') for _ in range(N)]
for l in lines[2:-1]:
    s, e, w = map(int, l.split(" "))
    maps[s].append((e, w))
start, end = map(int, lines[-1].split(" "))
fee[start-1] = 0
heappush(heap, (fee[start-1], start))
while heap:
    w, s = heappop(heap)
    nxt = maps[s]
    for n, nw in nxt:
        if fee[n-1] > w+nw:
            fee[n-1] = w+nw
            heappush(heap, (w+nw, n))
print(fee[end-1])