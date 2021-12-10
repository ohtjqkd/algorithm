# input
# 3 3
# 1 2 1
# 2 3 2
# 1 3 3
# output
# 3
import heapq
import sys
input = sys.stdin.readline
V, E = list(map(int, input().split(" ")))

parent = {}
rank = {}
heap = []
ret = 0
for _ in range(E):
    node_1, node_2, weight = list(map(int, input().split(" ")))
    parent[node_1], parent[node_2] = node_1, node_2
    rank[node_1], rank[node_2] = 0, 0
    heapq.heappush(heap, (weight, node_1, node_2))

def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_1, node_2):
    root_1 = find(node_1)
    root_2 = find(node_2)

    if rank[root_1] > rank[root_2]:
        parent[root_2] = root_1
    else:
        parent[root_1] = root_2
        if rank[root_1] == rank[root_2]:
            rank[root_2] += 1

while heap:
    weight, node_1, node_2 = heapq.heappop(heap)
    if find(node_1) != find(node_2):
        ret += weight
        union(node_1, node_2)
print(ret)
