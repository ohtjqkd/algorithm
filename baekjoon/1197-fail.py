import heapq

V, E = list(map(int, input().split(" ")))

parent = {i+1:i+1 for i in range(V)}
heap = []
ret = 0
for _ in range(E):
    node_1, node_2, weight = list(map(int, input().split(" ")))
    heapq.heappush(heap, (weight, node_1, node_2))

def get_parent(node):
    while node != parent[node]:
        node = parent[node]
    return node
    # if node == parent[node]:
    #     return node
    # return get_parent(parent[node])

def join(node_1, node_2):
    parent_1, parent_2 = get_parent(node_1), get_parent(node_2)
    if parent_1 == parent_2:
        return False
    elif node_1 > parent_2:
        parent[parent_2] = node_1
        return True
    else:
        parent[parent_1] = node_2
        return True

while heap:
    weight, node_1, node_2 = heapq.heappop(heap)
    if join(node_1, node_2):
        ret += weight
    # print(parent)
print(ret)

# input

# 3 3
# 1 2 1
# 2 3 2
# 1 3 3