# 트리

# 기본적으로 O(N)으로 해결하기 위해 풀이를 작성함
# for에서 O(N) dfs에서 O(N)이므로 O(N) + O(N) -> O(N)?


N = int(input())
parent = list(map(int, input().split(" ")))
T = int(input())
answer = 0

# 간선정보를 담기 위한 dictionary
edges = dict()

for i in range(len(parent)):
    # root 노드의 인덱스를 저장 root가 꼭 0이란 법이 없지..
    if parent[i] == -1:
        root = i
        continue
    # 지워지는 노드를 참조하는 간선은 의도적으로 배제함
    if i == T or parent[i] == T:
        continue
    # 나머지 간선에 대한 정보를 dictionary에 저장 {부모: [자식노드들]} 
    # 인덱스 접근이기 때문에 dict가 아닌 list도 사용가능할 듯
    edges[parent[i]] = edges.get(parent[i], []) + [i]

# dfs를 통해 리프 노드를 탐색

# 루트노드로 초기화
nodes = [root] 
if root == T: # 만약 제거할 노드가 루트노드라면 제거해줌.
    nodes.pop()

while nodes:
    curr_node = nodes.pop()
    nxt_nodes = edges.get(curr_node, False)
    if not nxt_nodes: # 다음 노드가 없으면 결과에 + 1
        answer += 1
    else: # 그렇지 않다면 자식 노드들을 스택에 추가해줌
        nodes.extend(nxt_nodes)
print(answer)