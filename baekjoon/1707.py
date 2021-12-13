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

def solution(edges, nodes, start):
    color = 1
    nodes[start] = color
    stack = [(i, nodes[i])]
    while stack:
        curr_node, curr_color = stack.pop()
        adjacents = edges[curr_node]
        for a in adjacents:
            if nodes[a] == curr_color:
                return False
            elif nodes[a] == 0:
                nodes[a] = curr_color*(-1)
                stack.append((a, nodes[a]))
            else:
                continue
    return True

for _ in range(K):
    V, E = map(int, input().split(" "))
    edges = [[] for _ in range(V)]
    for _ in range(E):
        n1, n2 = map(int, input().split(" "))
        edges[n1-1].append(n2-1)
        edges[n2-1].append(n1-1)
    visited = [0 for _ in range(V)]
    for i in range(V):
        if visited[i] == 0:
            if not solution(edges, visited, i):
                print("NO")
                break
    else:
        print("YES")