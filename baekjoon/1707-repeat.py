# input
# 2
# 3 2
# 1 3
# 2 3
# 4 4
# 1 2
# 2 3
# 3 4
# 4 2
# output
# YES
# NO
from collections import defaultdict
import sys
input = sys.stdin.readline
K = int(input())

def solution(edges, nodes):
    color = 1
    nodes[0] = color
    stack = [(0, nodes[0])]
    while stack:
        curr_node, curr_color = stack.pop()
        adjacents = edges[curr_node]
        for a in adjacents:
            if nodes[a] == curr_color:
                return "NO"
            elif nodes[a] == 0:
                nodes[a] = curr_color*(-1)
                stack.append((a, nodes[a]))
            else:
                continue
    return "YES"

for _ in range(K):
    V, E = map(int, input().split(" "))
    edges = [[] for _ in range(V)]
    for _ in range(E):
        n1, n2 = map(int, input().split(" "))
        edges[n1-1].append(n2-1)
        edges[n2-1].append(n1-1)
    print(solution(edges, [0 for _ in range(V)]))