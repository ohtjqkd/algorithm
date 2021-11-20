from collections import defaultdict
from heapq import heappop, heappush
import time
def solution(n, start, end, roads, traps):
    answer = 0
    origin_dir = defaultdict(list)
    reverse_dir = defaultdict(list)
    distances = [[float('inf'), float('inf')] for _ in range(n+1)]
    is_trap = [False for _ in range(n+1)]
    for t in traps:
        is_trap[t] = True
    for p, q, s in roads:
        origin_dir[p].append((q, s))
        reverse_dir[q].append((p, s))
    total_dir = {
        1:origin_dir,
        0:reverse_dir
    }
    heap = []
    heappush(heap, (0, start, 1)) # (weight, node, direction)
    distances[start][1] = 0
    while heap:
        w, n, d = heappop(heap)
        
        print(w, n, d)
        for next_node, weight in total_dir.get(d).get(n, []):
            dd = d
            if distances[next_node][d] > w+weight:
                if is_trap[next_node]:
                    dd = abs(d-1)
                distances[next_node][dd] = w+weight
                heappush(heap, (w+weight, next_node, dd))
        if distances[end][0] != float('inf') or distances[end][1] != float('inf'):
            break
        print(heap, distances)
        time.sleep(5)
    return min(distances[end])

tc = [
    [3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2], 5],
    [4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3], 4]
]
for t in tc:
    result = t[5]
    solution(t[0], t[1], t[2], t[3], t[4])
    print(f'expected answer: {result}, my answer: {solution(t[0], t[1], t[2], t[3], t[4])}')