# 트리의 부모 찾기

# 간선의 정보가 최대 100,000이기 때문에 O(N) 혹은 O(NlogN)의 시간 복잡도를 요구할 듯

N = int(input())

edges = [[] for _ in range(N+1)] # 간선 정보 저장을 위한 list
parent = [0] * (N + 1) # 부모 노드의 정보를 저장하기 위한 list
visited = [0] * (N + 1) # 이미 사용된 노드인지 체크하기 위한 list

# 주어지는 간선 정보에서 방향성을 알 수 없기 때문에 일단 후보로 넣어둠
for _ in range(N - 1):
    a, b = map(int, input().split(" "))
    edges[a].append(b)
    edges[b].append(a)
    
nodes = [1] # root 노드로 시작하기 위해 초기화
while nodes:
    curr = nodes.pop()
    visited[curr] = 1 # 사용된 노드들은 1로 체크해줌
    children = edges[curr] # 간선 정보 list에서 curr와 연결된 모든 노드를 가져옴
    for child in children:
        if visited[child] == 1: # 이미 체크 된 노드는 패스
            continue
        parent[child] = curr # 체크가 된 노드가 아니라면 curr가 child의 부모 노드라는 의미
        nodes.append(child)

for i in range(2, N + 1): # 2번 노드부터 하나씩 출력
    print(parent[i])

# 정답은 나왔으나 너무 느림...