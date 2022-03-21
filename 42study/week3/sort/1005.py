# ACM Craft

# 트리개념을 사용한 정렬방법이 필요한 듯 -> 위상정렬?
# 위상정렬의 핵심아이디어는 진입차수를 카운트하고, 순회하는 과정에서 진입차수가 0이 아닌 경우는 그 다음 과정을 진행하지 않도록 한다.
# 해당 문제를 처음에는 최단 경로처럼 풀었는데 시간 초과가 나는 이유는 아직 모르겠음..

import sys
from collections import deque

input = sys.stdin.readline

T = int(input()) # Test case

def bfs(): # 함수화
    N, K = map(int, input().split(" "))
    D = list(map(int, input().split(" "))) # [D_1, D_2, D_3, ... , D_n]

    edges = [[] for _ in range(N + 1)] # 간선정보 저장 List
    indegree = [0] * (N + 1) # 진입차수 카운터
    cost = [0  if i == 0 else D[i - 1] for i in range(N + 1)] # 해당 건물을 건축하는데까지 걸리는 가장 빠른 시간
    for _ in range(K):
        x, y = map(int, input().split(" "))
        indegree[y] += 1 # x에서 y로 진입하기 때문에 y의 진입차수를 1 증가시켜줌 
        edges[x].append(y) # 간선정보를 저장
    W = int(input()) # 목표건물
    q = deque([i for i in range(1, N + 1) if indegree[i] == 0]) # 진입차수가 0이라는 것은 의존하는 노드가 없음을 의미한다.(초기에 건설가능한 건물)
    while q:
        curr = q.popleft()
        children = edges[curr] # 현재 건물에 의존적인 건물리스트를 불러옴
        for c in children:
            indegree[c] -= 1 # 간선 정보를 지워줌 (진입차수를 1감소시킴)
            if indegree[c] == 0: # 만약 진입차수가 0이 된다면 모든 부모 건물들을 순회했다는 의미이므로 다음 과정을 진행할 수 있다.
                q.append(c)
            cost[c] = max(cost[c], cost[curr] + D[c - 1]) # 시간을 계속 갱신시켜줌
    return cost[W] # 목표로하는 건물의 시간을 return


for _ in range(T):
    print(bfs())