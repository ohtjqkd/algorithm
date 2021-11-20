import heapq
from copy import deepcopy

tc = int(input())


# def process(pages, cost):
#     ret = float('inf')
#     if len(pages) == 1:
#         return pages[0] + cost

#     for i in range(len(pages)-1):
#         new_arr = deepcopy(pages)
#         print(new_arr)
#         new_arr = new_arr[:i] + [new_arr[i]+new_arr[i+1]] + new_arr[i+2:]
#         ret = min(ret, process(new_arr, cost+pages[i]+pages[i+1]))
#     return ret


# for i in range(tc):
#     total = int(input())
#     pages = list(map(int, input().split(" ")))
#     print(process(pages, 0))

for _ in range(tc):
    total = input()
    C = list(map(int, input().split(" ")))
    # heap = []
    # for c in C:
    #     heapq.heappush(heap, c)
    heapq.heapify(C)
    ret = 0
    while len(C) > 1:
        print(C)
        merged = heapq.heappop(C)+heapq.heappop(C)
        ret += merged
        heapq.heappush(C, merged)
        print(ret)
    print(ret)