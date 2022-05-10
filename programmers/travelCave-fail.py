from collections import defaultdict, deque

# def makeTree(adjacent, order_v, n):
#     visited = [0 for _ in range(n)]
#     tree = dict()
#     need_visit = deque([0])
#     repeat = [0 for _ in range(n)]
#     max_repeat = 0
#     while need_visit:
#         now_node = need_visit.pop()
#         if order_v.get(now_node) and not visited[order_v[now_node]]:
#             need_visit.appendleft(now_node)
#             repeat[now_node] += 1
#             if repeat[now_node] > 5:
#                 break
#             continue
#         visited[now_node] = 1
#         children = adjacent[now_node]
#         for child in children:
#             if not visited[child]:
#                 need_visit.append(child)

#     answer = True if n == sum(visited) else False
#     return answer


# def solution(n, path, order):

#     adjacent = defaultdict(list)
#     order_visit = defaultdict()
#     for node in path:
#         a, b = node
#         adjacent[a].append(b)
#         adjacent[b].append(a)
#     for o in order:
#         order_visit[o[1]] = o[0]
#     return makeTree(adjacent, order_visit, n)



n, path, order = 9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]
n, path, order = 9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]
n, path, order = 9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]

def solution(n, path, order):
    adjacent = defaultdict(list)
    visited, locked = [0] * (n + 1), [False] * n
    priority_room, parent = [-1] * (n + 1), [-1] * n
    adjacent[-1].append(0)
    for a, b in path:
        adjacent[a].append(b)
        adjacent[b].append(a)
    for o in order:
        priority_room[o[0]] = o[1]
        locked[o[1]] = True
    # parent 정보 저장
    stack = [0]
    while stack:
        curr = stack.pop()
        for nxt in adjacent.get(curr, []):
            if visited[nxt] == 0:
                visited[nxt] = 1
                stack.append(nxt)
                parent[nxt] = curr

    stack = [0]
    while stack:
        # print(stack)
        curr = stack.pop()
        visited[curr] = 0
        is_priority_room = priority_room[curr]
        if is_priority_room != -1:
            locked[is_priority_room] = False
            if visited[parent[is_priority_room]] == 0:
                stack.append(is_priority_room)
                # visited[is_priority_room] = 0
        else:
            for nxt in adjacent.get(curr, []):
                if visited[nxt] == 1 and not locked[nxt]:
                    stack.append(nxt)
                    # visited[nxt] = 0
        # print(visited)
    return sum(visited) == 0

print(solution(n, path, order))
