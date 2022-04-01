# 문제 추천 시스템 version2

# 더 몰라
import heapq as hq
import sys

input = sys.stdin.readline

N = int(input())
min_h = []
max_h = []
for _ in range(N):
    num, rank, alg = list(map(int, input().rstrip().split(" ")))
    hq.heappush(min_h, (rank, num, alg))
    hq.heappush(max_h, (-rank, -num, alg))

M = int(input())
for _ in range(M):
    line = list(input().split(" "))
    com = line[0]
    if com == "add":
        num, rank, alg = line[1:]
        hq.heappush(min_h, (rank, num, alg))
        hq.heappush(max_h, (-rank, -num, alg))
