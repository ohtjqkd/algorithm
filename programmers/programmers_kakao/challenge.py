from collections import deque
from copy import deepcopy

from scipy.stats import stats

n, z, roads, queries = 5, 5,	[[1,2,3],[0,3,2]], [0,1,2,3,4,5,6]
# def solution(n, z, roads, queries):
#     road_info = dict()
#     max_q = max(queries)
#     movement = [0 for _ in range(max_q+1)]
#     stack = deque() # 현재 위치, 움직인 횟수, 가중치
#     stack.append([0,0,0])
#     result = [0 for _ in range(len(queries))]
#     for r in roads:
#         road_info[(r[0], r[1])], road_info[(r[1], r[0])] = r[2], r[2]
#     print(road_info)
#     until = [0 for i in range(max([queries[i] % z for i in range(len(queries))]))]
#     visited = deepcopy(until)
#     print(until)
#     while stack:
#         now = stack.popleft()
#         print(until)
#         print(now[1], until[now[2]])
#         if now[1] > until[now[2]-1]:
#             pass
#         else:
#             until[now[2]-1] = now[1]
#         print(now)
#         # for idx, q in enumerate(queries):
#         # newQueries = []
#         # while queries:
#         #     poped = queries.pop()
#             # if (poped-now[2]) % z == 0:
#                 # result[idx] = q-now[2] % z + now[1]
#         for i in range(n):
#             isExist = road_info.get((now[0], i)) 
#             if now[0] == i and now[2]+z < len(until):# and until[now[2]+z] == 0:
#                 stack.append([now[0], now[1]+1, now[2]+z])
#             elif isExist and now[2]+isExist < len(until):# and until[now[2]+isExist] == 0:
#                 stack.append([i, now[1]+1, now[2]+isExist])
#             else:
#                 stack.append([i, now[1]+1, now[2]])
#     # print(movement)
#     # answer = []
#     answer = 0
#     return answer

def solution(n, z, roads, queries):
    comb_cand = set()
    comb_cand.add(z)
    maxq = max(queries)

    for r in roads:
        comb_cand.add(r[2])
    comb_cand = [[i, 0] for i in comb_cand]
    print(comb_cand)
    print(comb_cand)

def findComb(comb_cand):
    poped = comb_cand.pop()
    mins, maxs = 0, 
solution(n,z,roads,queries)
# def dfs(n, z, max_q, road_info, now, cnt, movement, z, moveCnt):
    
#     if cnt > max_q:
#         return
    # for i in range()
    

# solution(n, z, roads, queries)
# test = [0 for _ in range(10**18)]
result = [0,-1,1,2,3,1,4]

from scipy import stats

print(1 - stats.binom.cdf(0, n = 3, p = 0.2))
print(stats.poisson.cdf(2, mu = 3))