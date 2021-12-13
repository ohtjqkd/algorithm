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
from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())
maps = [[] for _ in range(N+1)]
fee = [INF for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split(" "))
    maps[s].append((e, w))
start, end = map(int, input().split(" "))

heap = []
fee[start] = 0
heappush(heap, (fee[start], start))

while heap:
    w, s = heappop(heap)
    if fee[s] < w:
        continue
    for n, nw in maps[s]:
        nw += w
        if fee[n] > nw:
            fee[n] = nw
            heappush(heap, (nw, n))
print(fee[end])