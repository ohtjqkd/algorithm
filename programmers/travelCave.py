from collections import defaultdict, deque


n, path, order = 9, [[0, 1], [0, 3], [0, 7], [8, 1], [
    3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]

n, path, order = 9, [[0, 1], [0, 3], [0, 7], [8, 1], [
    3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]


def makeTree(adjacent, order_v, n):
    visited = [0 for _ in range(n)]
    tree = dict()
    need_visit = deque([0])
    repeat = [0 for _ in range(n)]
    max_repeat = 0
    while need_visit:
        now_node = need_visit.pop()
        if order_v.get(now_node) and not visited[order_v[now_node]]:
            need_visit.appendleft(now_node)
            repeat[now_node] += 1
            if repeat[now_node] > 5:
                break
            continue
        visited[now_node] = 1
        children = adjacent[now_node]
        for child in children:
            if not visited[child]:
                need_visit.append(child)

    answer = True if n == sum(visited) else False
    return answer


def solution(n, path, order):

    adjacent = defaultdict(list)
    order_visit = defaultdict()
    for node in path:
        parent, child = node[0], node[1]
        adjacent[parent].append(child)
        adjacent[child].append(parent)
    for o in order:
        order_visit[o[1]] = o[0]
    return makeTree(adjacent, order_visit, n)


print(solution(n, path, order))
