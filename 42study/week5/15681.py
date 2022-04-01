# 트리와 쿼리

# 노드의 수가 10^5이므로 O(N^2)은 절대 안됨 (O(N) or O(NlongN))으로 풀이해야함
# leaf node부터 시작하여 child node의 sub node 갯수를 부모노드에 더해주는 방식으로 풀이함
# 재귀로 풀려했으나 recursive가 남 왜지?? limit를 10^6까지 풀어줬으나 터져벌.임
# 후위순회를 stack으로 구현하기가 어려웠음

import sys
input = sys.stdin.readline
N, R, Q = map(int, input().split(" "))

edges = [[] for _ in range(N)] # 간선정보
sub_node = [1] * N  # 각 노드의 sub node 갯수를 저장하는 list
parent = [-1] * N   # 각 노드의 parent node를 저장하는 list 이후 후위순회를 위해서도 이용됨 like visited
for _ in range(N - 1):
    a, b = map(int, input().split(" "))
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

stack = [R - 1] # root node부터 시작



while stack:
    curr = stack[-1] # 자식노드들이 다 처리되기 전까지는 제거하지 않는다.
    if len(edges[curr]) == 1 and curr != R - 1 \
        or (parent[curr] != -1 and sub_node[curr] != 1): # 윗줄은 leaf node 판별을 위한 조건, 아랫줄은 자식노드들이 처리가 됐는지 판별하기 위함
        curr = stack.pop() # leaf node 혹은 sub node들이 모두 처리됐다면 stack에서 제거
        sub_node[parent[curr]] += sub_node[curr] # current node의 sub node 갯수를 parent node의 sub node 갯수에 더해줌
    else: # leaf node도 아니고 sub node들이 처리되지 않았다면
        for child in edges[curr]: # child node를 stack에 append
            if parent[child] == -1 and child != R - 1: # parent[child] != -1이면 이미 stack에 append됐다는 의미 but 뒤에 조건이 없다면 root가 계속 append됨..
                stack.append(child)
                parent[child] = curr
    if len(stack) == 1: #len(stack) == 1이라는 의미는 모든 sub node를 처리했거나 root노드만 있는 경우이므로 stack에서 제거해주고 반복문을 종료해준다.
        stack.pop()

for _ in range(Q):
    print(sub_node[int(input()) - 1])









# recursion error = =;
# def dfs(node, sub_node, edges, parent):
#     if len(edges[node]) == 1 and node != R - 1:
#         sub_node[parent[node]] += sub_node[node]
#     else:
#         for child in edges[node]:
#             if parent[child] == -1 and child != R - 1:
#                 parent[child] = node
#                 dfs(child, sub_node, edges, parent)
#         if node != R - 1:
#             sub_node[parent[node]] += sub_node[node]
#     return

# dfs(R - 1, sub_node, edges, parent)
# for _ in range(Q):
#     print(sub_node[int(input()) - 1])