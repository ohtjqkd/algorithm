# 19
# 1 2 3
# 2 4 5
# 3 6 7
# 4 8 -1
# 5 9 10
# 6 11 12
# 7 13 -1
# 8 -1 -1
# 9 14 15
# 10 -1 -1
# 11 16 -1
# 12 -1 -1
# 13 17 -1
# 14 -1 -1
# 15 18 -1
# 16 -1 -1
# 17 -1 19
# 18 -1 -1
# 19 -1 -1

N = int(input())
edge_info = [list(map(int, input().split(" "))) for _ in range(N)]
print(edge_info)
edges = [None for _ in range(10001)]
root_check = [1 for _ in range(10001)]
for c, l, r in edge_info:
    edges[c] = [l, r]
    if l != -1:
        root_check[l] = 0
    if r != -1:
        root_check[r] = 0
for i in range(1, 10001):
    if root_check[i] == 1:
        ROOT = i
        break

left_node = [0 for _ in range(10001)]
right_node = [0 for _ in range(10001)]

level_info = [[ROOT, ROOT]]

def dfs(node, level):
    if node == -1:
        return 0
    if len(level_info) < level + 1:
        level_info.append([node, node])
    else:
        level_info[level][0], level_info[level][1] = min(level_info[level][0], node), max(level_info[level][1], node)
    left_node[node] = dfs(edges[node][0], level + 1)
    right_node[node] = dfs(edges[node][1], level + 1)
    return left_node[node] + right_node[node] + 1

dfs(ROOT, 0)
print(left_node)
print(right_node)
print(level_info)
ret = 0
ret_level = 0
for idx, (left, right) in enumerate(level_info):
    if left == right:
        continue
    else:
        sum = 1
        node = ROOT
        for _ in range(idx):
            if edges[node][0] != -1 or node == left:
                if node != ROOT:
                    sum += right_node[node] + 1
                node = edges[node][0]
            elif edges[node][1] != -1:
                node = edges[node][1]
        node = ROOT
        for _ in range(idx):
            if edges[node][1] != -1 or node == right:
                if node != ROOT:
                    sum += left_node[node] + 1
                node = edges[node][1]
            elif edges[node][0] != -1:
                node = edges[node][0]
        if ret < sum:
            print(idx, sum)
            ret = sum
            ret_level = idx
print(ret, ret_level + 1)