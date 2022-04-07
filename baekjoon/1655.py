# 가운데를 말해요
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

max_heap = []
min_heap = []

N = int(input())
for _ in range(N):
    value = int(input())
    if not max_heap:
        heappush(max_heap, -value)
        print(value)
        continue
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -value)
    elif len(max_heap) - len(min_heap) == 1:
        heappush(min_heap, value)
    if -max_heap[0] > min_heap[0]:
        max_pop = heappop(max_heap)
        min_pop = heappop(min_heap)
        heappush(min_heap, -max_pop)
        heappush(max_heap, -min_pop)
    print(-max_heap[0])




#
# def find_idx(tree, value):
#     start, end = 0, len(tree)
#     while start < end:
#         mid = (start + end) // 2
#         if tree[mid] < value:
#             start = mid + 1
#         elif tree[mid] > value:
#             end = mid - 1
#         else:
#             break
#     return (start + end) // 2

# N = int(input())
# for _ in range(N):
#     value = int(input())
#     idx = find_idx(tree, value) + 1
#     tree = tree[:idx] + [value] + tree[idx:]
#     print(tree[len(tree)//2 + len(tree) % 2 - 1])