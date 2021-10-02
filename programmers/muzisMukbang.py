import random
import datetime
from collections import deque
import heapq
# food_times, k = [3, 1, 2], 5
# food_times, k = [random.randint(1,100000000) for _ in range(200000)], random.randint(1, 2 * (10**13))
food_times, k = [4,2,3,6,7,1,5,8], 27
food_times, k = [4,2,3,6,7,1,5,8], 16
# k=16
# answer = 3
# print(food_times)
def solution(food_times, k):
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, [food_times[i],i+1])
    if sum(food_times) <= k:
        return -1
    prev_min = 0
    while heap:
        nowLength = len(heap)
        poped_min = heapq.heappop(heap)
        if prev_min == poped_min[0]:
            continue
        differ = (poped_min[0] - prev_min)
        if differ * nowLength > k:
            start, end = 0, differ
            while start < end:
                mid = (start + end)//2
                if mid * nowLength < k:
                    start = mid + 1
                else:
                    end = mid - 1
            min_value = mid
            k -= min_value * nowLength
            heapq.heappush(heap, poped_min)
            break
        else:
            k -= differ * nowLength
        prev_min = poped_min[0]
    result = list(heap)
    result.sort(key=lambda x: x[1])
    end = datetime.datetime.now()
    print(result)
    return result[k%len(result)][1]

print(solution(food_times, k))