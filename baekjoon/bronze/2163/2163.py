# input: 2 2, 1 1
# output: 3, 0
r, c = map(int, input().split(" "))
def dfs(r, c):
    if r == 1 and c == 1:
        return 0
    ret = 0
    if r < c:
        ret += dfs(r, c//2) + dfs(r, c-c//2)
    else:
        ret += dfs(r//2, c) + dfs(r-r//2, c)
    return ret + 1
print(dfs(r, c))
