from queue import PriorityQueue

from collections import deque
from heapq import heappop, heappush

for _ in range(int(input())):
    n, m = map(int, input().split(" "))
    heap, deq = [], deque([])
    arr = list(map(int, input().split(" ")))
    for i in range(n):
        deq.append((arr[i], i))
        heappush(heap, -arr[i])
    cnt = 1
    
    while heap and deq:
        if heap[0] == -deq[0][0]:
            if deq[0][1] == m:
                print(cnt)
                break
            else:
                heappop(heap)
                deq.popleft()
                cnt += 1
        else:
            deq.append(deq.popleft())
