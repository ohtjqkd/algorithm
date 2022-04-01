# 도시건설

# 이게 kruskal인가바 union find인데 기억이 안나
# 최소 spanning 유형은 kruskal or prim인데
# kruskal의 경우 O(elog2e) 복잡도이고, prim은 (O(N^2))이다.
# e = 간선의 개수, N은 정점의 개수
# 그래프에 간선의 개수가 많은 밀집 그래프의 경우 prim 알고리즘이 적합하고
# 적은 숫자의 간선을 가지는 희소 그래프의 경우 kruskal이 적합하다.

N, M = map(int, input().split(" "))
edges = []
total = 0
parent = [i for i in range(N + 1)]
rank = [0 for _ in range(N + 1)]
total, MR, R, ret, con = 0, 0, -1, 0, 0
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return False
    if rank[root_a] > rank[root_b]:
        rank[root_a] += 1
        parent[root_b] = root_a
    else:
        rank[root_b] += 1
        parent[root_a] = parent[b]
    return True
def find(a):
    # path compression
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

for i in range(M):
    a, b, w = map(int, input().split(" "))
    total += w
    edges.append((w, a, b))
edges.sort()
for edge in edges:
    w, a, b = edge
    if union(a, b):
        con += 1
        total -= w

if con != N - 1:
    print(-1)
else:
    print(total)

# 시간초과 pypy3 통과
# def find(a):
#     if parent[a] == a:
#         return a
#     parent[a] = find(parent[a])
#     return parent[a]

# def join(a, b):
#     root_a = find(a)
#     root_b = find(b)
#     if root_a == root_b:
#         return False
#     if rank[root_a] > rank[root_b]:
#         rank[root_a] += 1
#         parent[root_b] = root_a
#     else:
#         rank[root_b] += 1
#         parent[root_a] = parent[b]
#     return True

# for w, a, b in A:
#     if join(a, b):
#         ret += w

# max_rank = 0
# R = 0
# for i, r in enumerate(rank):
#     if max_rank < r:
#         max_rank = r
#         R = i

# for n in range(1, N+1):
#     if find(n) != R:
#         print(-1)
#         break
# else:
#     print(total - ret)