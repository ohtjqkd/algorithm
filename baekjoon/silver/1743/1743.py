# input
# 3 4 5
# 3 2
# 2 2
# 3 1
# 2 3
# 1 1
# output
# 4

from collections import deque

N, M, K = map(int, input().split(" "))
R = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split(" "))
    R[r-1][c-1] = 1

def dfs(r, c):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    R[r][c], ret = 0, 1
    stack = deque([(r, c)])
    while stack:
        r, c = stack.popleft()
        for i in range(4):
            rr, cc = r+dx[i], c+dy[i]
            if 0 <= rr < N and 0 <= cc < M and R[rr][cc] == 1:
                R[rr][cc] = 0
                ret += 1
                stack.append((rr, cc))
    return ret

ret = 0
for i in range(N):
    for j in range(M):
        if R[i][j] == 1:
            ret = max(ret, dfs(i, j))
print(ret)