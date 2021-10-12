# 미로는 N*M, (1<= N,M <= 100)
# 빈방 혹은 벽으로 이루어져 있음
# 벽은 부수지 않으면 이동할 수 없다.
# 운영진은 여러명이며 항상 모두 같은 방에 있어야 한다.
# 이동은 상하좌우 인접 방으로 가능하며 벽을 부수면 이동이 가능하다.
# (0, 0)에서 (N, M)까지 가려면 벽을 최소 몇 개 부서어야 하는지 구하여라
# * 이동 횟수와는 상관이 없는거 같다.

# input
# 6 6
# 001111
# 010000
# 001111
# 110001
# 011010
# 100010

N, M = list(map(int, input().split()))
maze = [input() for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
def dfs(x, y, visited, broken):
    print(x, y)
    if x == N-1 and y == M-1:
        print('broken walls:', broken)
        return broken        
    ret = float('inf')
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    visited[x][y] = 1
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0 <= xx < N and 0 <= yy < M and visited[xx][yy] == 0:
            if maze[xx][yy] == '1':
                broken += 1
            ret = min(ret, dfs(xx, yy, visited, broken))
    visited[x][y] = 0
    return ret

dfs(0, 0, visited, 0)