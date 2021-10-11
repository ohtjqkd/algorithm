from collections import defaultdict, deque

def solution(n, wires):
    def count_sub(pair, edges):
        visited = [0 for _ in range(n)]
        cnt = 0
        node_1, node_2 = pair
        stack = [node_1]
        while stack:
            cnt += 1
            poped = stack.pop()
            visited[poped-1] = 1
            next_nodes = edges[poped]
            for node in next_nodes:
                # 이미 방문한 노드이거나 끊고자하는 간선일 경우 continue
                if visited[node-1] == 1 or node == node_2:
                    continue
                stack.append(node)
        return cnt

    answer = float('inf')
    edges = defaultdict(list)
    for n1, n2 in wires:
        edges[n1].append(n2)
        edges[n2].append(n1)

    for w in wires:
        count = count_sub(w, edges)
        answer = min(answer, abs(n-2*count))
    return answer





test = [[4, [[1, 2], [1,3], [1,4]], 2], [9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]],3], [4,[[1,2],[2,3],[3,4]],0], [7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]], 1]]
for t in test:
    print('test', solution(t[0], t[1]))