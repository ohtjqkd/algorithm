# input
# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32
# output
# 0
# 1
# 2
# 12345678
# 0

import heapq, sys
input = sys.stdin.readline
N = int(input())
# heap = []
# for _ in range(N):
#     C = int(input())
#     if C == 0:
#         try:
#             print(heapq.heappop(heap))
#         except:
#             print(0)
#     else:
#         heapq.heappush(heap, C)

# heap 구현

heap = []
def push(heap, v):
    heap.append(v)
    idx = len(heap)-1
    if idx == 0:
        return
    else:
        while idx > 0:
            child, parent = heap[idx], heap[idx//2]
            if child < parent:
                heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            else:
                break
def pop(heap):
    if len(heap) == 0:
        return 0
    elif len(heap) == 1:
        return heap.pop()
    pop_value = heap[0]
    heap[0] = heap.pop()
    parent = 0
    while True:
        left, right = parent*2+1, parent*2+2
        if left >= len(heap):
            break
        if right >= len(heap):
            if heap[parent] > heap[left]:
                heap[parent], heap[left] = heap[left], heap[parent]
                parent = left
            else:
                break
        else:
            if heap[parent] < heap[left] and heap[parent] < heap[right]:
                break
            elif heap[left] < heap[right]:
                heap[parent], heap[left] = heap[left], heap[parent]
                parent = left
            else:
                heap[parent], heap[right] = heap[right], heap[parent]
                parent = right
    return pop_value    

for _ in range(N):
    C = int(input())
    if C == 0:
        print(pop(heap))
    else:
        push(heap, C)


        