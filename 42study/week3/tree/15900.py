# 나무탈출

import sys

input = sys.stdin.readline
N = int(input())
answer = 0
visited = [0 for _ in range(N)]
edges = [[] for _ in range(N)]

# 방향성을 알 수 없기 때문에 일단 양방향으로 간선정보를 저장
for _ in range(N - 1):
    a, b = map(int, input().split(" "))
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

# 현재 노드와 깊이(?)를 알 수 있게 하기 위해 튜플 혹은 배열로 저장
nodes = [(0, 0)]
while nodes:
    curr, depth = nodes.pop()
    is_leaf = True # 현재 노드가 leaf인지 판단하는 flag
    visited[curr] = 1 # 현재 노드를 방문 처리해줌
    children = edges[curr] 
    for c in children:
        if visited[c] == 1: # 자식 노드를 순회하면서 이미 방문됐던 노드라면 처리하지 않고 지나간다.
            continue
        is_leaf = False # 방문하지 않은 노드가 하나라도 있으면 leaf노드가 아니기 때문에 flag를 False로 갱신
        nodes.append((c, depth + 1)) # depth를 1 증가시켜 stack에 넣어줌
    if is_leaf:
        answer += depth # 만약 leaf라면 현재의 depth를 answer에 더해줌
print(answer)
if answer % 2 == 1:
    print("YES")
else:
    print("NO")
