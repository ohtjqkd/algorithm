# input
# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13
# output
# 7
# 8
# 10
# 13
# 19
# 20
# 23

# small = []
# for _ in range(9):
#     small.append(int(input()))

# S = sum(small)

# for i in range(len(small)-1):
#     for j in range(i+1, len(small)):
#         if small[i]+small[j] == S-100:
#             del(small[j])
#             del(small[i])
#             break
# small.sort()
# for s in small:
#     print(s)

small_height = [int(input()) for _ in range(9)]
small_height.sort()
visited = set()
def dfs(rest, idx, visited: set):
    if (len(visited) == 7):
        if rest == 0:
            return visited
        return
    for i in range(idx + 1, 9):
        if rest - small_height[i] < 0:
            break
        else:
            visited.add(small_height[i])
            ret = dfs(rest - small_height[i], i, visited)
            if (ret):
                return ret
            visited.remove(small_height[i])
ret = sorted(list(dfs(100, -1, visited)))
for r in ret:
    print(r)