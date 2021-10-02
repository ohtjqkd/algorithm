class Node:
    def __init__(self, name):
        self.__setattr__(name, "hi")
node = Node("next1")
print(node.next1)
a, edges=[-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]
a, edges=[-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]
from collections import defaultdict
def solution(a, edges):
    if sum(a) != 0:
        return -1
    answer = 0
    visited = [0 for _ in range(len(a))]
    node_v = defaultdict(int)
    parent = dict()
    tree = defaultdict(list)
    adj = defaultdict(list)
    # node value init
    for i in range(len(a)):
        node_v[i] = a[i]

    #edges info init
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    stack = []
    stack.append(edges[0][0])

    #make tree
    while stack:
        poped = stack.pop()
        visited[poped] = 1
        if adj.get(poped) == None:
            continue
        nexts = adj.get(poped)
        for n in nexts:
            if visited[n] == 1:
                continue
            else:
                tree[poped].append(n)
                parent[n] = poped
                stack.append(n)
    # dfs not using recursion
    stack, newStack = [], []
    stack.append(edges[0][0])
    newStack.append(edges[0][0])
    while stack:
        print(stack)
        now = stack.pop()
        if tree.get(now) == None:
            continue
        nexts = tree.get(now)
        stack.extend(nexts)
        newStack.extend(nexts)
    while newStack:
        now = newStack.pop()
        if now == edges[0][0]: break
        a[parent[now]] += a[now]
        answer += abs(a[now])
    return answer
    # if sum(a) != 0:
    #     return -1
    # answer = 0
    # visited = [0 for _ in range(len(a))]
    # node_v = dict()
    # tree = defaultdict(list)
    # adj = defaultdict(list)
    # # node value init
    # for i in range(len(a)):
    #     node_v[i] = a[i]

    # #edges info init
    # for e in edges:
    #     adj[e[0]].append(e[1])
    #     adj[e[1]].append(e[0])
    # stack = []
    # stack.append(edges[0][0])

    # #make tree
    # while stack:
    #     poped = stack.pop()
    #     visited[poped] = 1
    #     next = adj.get(poped)
    #     for n in next:
    #         if visited[n] == 1:
    #             continue
    #         else:
    #             tree[poped].append(n)
    #             stack.append(n)
    # answer = dfs(tree, node_v, -1, edges[0][0])
    # # print(node_v)
    # # print(tree)
    # return answer

def dfs(tree, node_v, prev, now):
    answer = 0
    print(tree, node_v, prev, now)
    # print(node_v)
    if not tree.get(now):
        now_v = node_v.get(now)
        node_v[prev] += now_v
        answer += abs(now_v)
        return answer
    nexts = tree.get(now)
    print("nexts", nexts)
    for nxt in nexts:
        answer += dfs(tree, node_v, now, nxt)
    if prev == -1:
        return answer
    now_v = node_v.get(now)
    node_v[prev] += now_v
    answer += abs(now_v)
    return answer

print(5 * False)
print(solution(a, edges))