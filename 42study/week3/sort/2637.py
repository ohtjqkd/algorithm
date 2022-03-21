# 장난감 조립

# 앞선 위상 정렬과 알고리즘은 같다.
# 하지만 하나의 중간 제품 혹은 완제품을 만드는데에 이전 단계의 조합(?)을 통해 만들어지기 때문에 1차원 배열로 처리하기 어려움
# 따라서 cost와 weight를 2차원 배열로 만들어 처리하였음

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
indeg = [0] * N 

# 다음 단계의 제품을 만들기 위해 필요한 해당 단계의 제품의 수
# ex) 4번 제품이 6번과 7번을 만드는데 쓰이고, 각각 4개, 5개가 필요하다면 weight[3][5] = 4, weight[3][6] = 5
weight = [[0] * N for _ in range(N)]
cost = [[0] * N for _ in range(N)]
edges = [[] for _ in range(N)]
for _ in range(M):
    x, y, k = list(map(int, input().split(" ")))
    edges[y-1].append(x-1)
    indeg[x-1] += 1
    weight[y-1][x-1] = k

# 마지막 출력에 사용하기 위해 base_part를 미리 저장
base_part,q = [], [] 
for i in range(N):
    if indeg[i] == 0:
        base_part.append(i)
        q.append(i)

# base part의 개수를 1로 초기화해줌
for i in base_part:
    cost[i][i] = 1

while q:
    curr = q.pop()
    C = cost[curr] # curr 제품을 만드는데 들어가는 제품의 개수
    for c in edges[curr]:
        indeg[c] -= 1
        if indeg[c] == 0: # 진입차수가 0이 되는 순간의 cost[c]가 완성됨, 다음 단계를 진행할 수 있다(?)
            q.append(c)
        for i, v in enumerate(C):
            cost[c][i] += v * weight[curr][c] # c 제품을 만드는데 curr 제품이 weight[curr][c]만큼 쓰여지기 때문에 곱연산을 통해 더해줌
for b in base_part:
    print(b+1, cost[N-1][b])
