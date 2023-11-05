# input
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
# output
# ABDCEFG
# DBAECFG
# DBEGFCA
tree = {}
def dfs(node, pre, ino, post):
    if node == ".":
        return
    left, right = tree[node]["left"], tree[node]["right"]
    pre.append(node)
    dfs(left, pre, ino, post)
    ino.append(node)
    dfs(right, pre, ino, post)
    post.append(node)
    return pre, ino, post
N = int(input())
edge = []
for _ in range(N):
    edge.append(input().split(" "))
    
for p, l, r in edge:
    tree[p] = {}
    tree[p]["left"], tree[p]["right"] = l, r
pre, ino, pos = dfs(edge[0][0], [], [], [])
print(''.join(pre))
print(''.join(ino))
print(''.join(pos))