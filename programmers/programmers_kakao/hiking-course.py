from heapq import heappush, heappop
import sys

sys.setrecursionlimit = 1000
def solution(n, paths, gates, summits):
    answer = []
    to_summit = [i for i in range(n + 1)]
    to_gate = [i for i in range(n + 1)]
    def find(node, to, tmp = 200):
        if node != to[node]:
            to[node] = find(to[node], to)
        return to[node]
    def union(a, b, to, is_in):
        if b in is_in:
            return to
        to[b] = a
        return to
    is_summit = set(summits)
    is_gate = set(gates)
    heap = []
    for a, b, w in paths:
        heappush(heap, (w, a, b))
    while heap:
        w, a, b = heappop(heap)
        to_gate_a, to_summit_a = find(a, to_gate), find(a, to_summit)
        to_gate_b, to_summit_b = find(b, to_gate), find(b, to_summit)
        if to_gate_a in is_gate and to_summit_b in is_summit:
            answer.append([to_summit_b, w])
        if to_gate_b in is_gate and to_summit_a in is_summit:
            answer.append([to_summit_a, w])
        if to_gate_a in is_gate:
            to_gate = union(a, b, to_gate, is_gate)
        else:
            to_gate = union(b, a, to_gate, is_gate)
        if to_summit_a in is_summit and to_summit_b in is_summit:
            if to_summit_a > to_summit_b:
                to_summit = union(b, a, to_summit, is_summit)
            else:
                to_summit = union(a, b, to_summit, is_summit)
        elif to_summit_a in is_summit:
            to_summit = union(a, b, to_summit, is_summit)
        else:
            to_summit = union(b, a, to_summit, is_summit)
    
    answer.sort(key=lambda x: (x[1], x[0]))
    return answer[0]
    # for g in gates:
    #     heap.append([0, g])
    #     # heappush(heap, [0, g])
    # while heap:
    #     curr_weight, curr = heap.pop()
    #     for next_node, weight in path[curr]:
    #         if weight < curr_weight:
    #             weight = curr_weight
    #         if weights[next_node] <= weight:
    #             continue
    #         weights[next_node] = min(weights[next_node], weight)
    #         if next_node in is_summit:
    #             continue
    #         else:
    #             heap.append([weight, next_node])
    #             # heappush(heap, [weight, next_node])
    # intensity = float('inf')
    # summit = -1
    # for s in summits:
    #     if weights[s] < intensity:
    #         summit, intensity = s, weights[s]
    # return [summit, intensity]

tc = [[6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5],	[5, 3]],
[7,	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],	[1],	[2, 3, 4],	[3, 4]],
[7,	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7],	[1, 5],	[5, 1]],
[5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],	[1, 2],	[5],	[5, 6]]]

for t in tc:
    print(solution(t[0], t[1], t[2], t[3]) == t[4])