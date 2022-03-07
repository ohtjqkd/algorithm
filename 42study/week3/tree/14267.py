# 회사 문화1

# 처음 접근은 트리를 만들고, 칭찬을 할 때마다 서브트리의 점수를 늘려가는 식으로 접근
# 하지만 그렇게 되면 1000 * 100000으로 시간초과가 나옴 ** O(N ^ 2)
# 다른 방법을 강구함
# dp에서 착안하여 칭찬을 받은 사원에만 먼저 점수를 더해주고 O(1000)
#                                                   +
# 그 이후 모든 노드를 순회하면서 칭찬점수를 누적시켜줌     O(100000)


n, m = map(int, input().split(" "))
boss = list(map(int, input().split(" ")))

score = [0] * n # 사원들의 칭찬점수를 저장할 list
edges = [[] for _ in range(n)] #간선정보
for i, b in enumerate(boss):
    if b == -1: # 사장의 경우 참조하는 직속상사가 없으므로 넘김
        continue
    edges[b - 1].append(i) # 상사의 노드에서 사원방향의 간선 정보를 저장 ** -1을 해준 이유는 index로 접근하기 위해서

# 먼저 칭찬 점수를 모두 더해줌
for _ in range(m):
    e, w = map(int, input().split(" "))
    score[e-1] += w # 같은 사람을 칭찬해줄 수 있다는 사실을 깨달았다!

# 사장부터 시작!
nodes = [0]
while nodes:
    curr = nodes.pop()
    children = edges[curr]
    for c in children:
        score[c] += score[curr] # 현재 노드의 점수를 자식 노드의 점수에 더해줌
        nodes.append(c)
print(' '.join(map(str, score)))

# 그런데 이렇게 해도 느림 왜지?

# 시간 초과 코드
# for _ in range(m):
#     e, w = map(int, input().split(" "))
#     nodes = [e]
#     while nodes:
#         curr = nodes.pop()
#         score[curr] += w
#         nodes.extend(edges[curr])