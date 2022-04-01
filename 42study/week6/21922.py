# # 학부 연구생 민상

# # 무지성 풀이

N, M = map(int, input().split(" "))

room = [list(map(int, input().split(" "))) for _ in range(N)]
ret_table = [[0] * M for _ in range(N)]
stack = []
for i in range(N):
    for j in range(M):
        if room[i][j] == 9:
            ret_table[i][j] = 1
            for k in range(4):
                stack.append((i, j, k))
mem = [[[0,0,0,0] for _ in range(M)] for _ in range(N)]
dir_table = [[0,1,2,3], [2,1,0,3], [0, 3, 2, 1], [3, 2, 1, 0], [1, 0, 3, 2]]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ret = 0
while stack:
    x, y, d = stack.pop()
    mem[x][y][d] = 1
    xx, yy = x + dx[d], y + dy[d]
    if 0 > xx or xx >= N or 0 > yy or yy >= M or room[xx][yy] == 9:
        continue
    next_dir = dir_table[room[xx][yy]][d]
    if not mem[xx][yy][next_dir]:
        ret_table[xx][yy] = 1
        stack.append((xx, yy, dir_table[room[xx][yy]][d]))

for i in range(N):
    for j in range(M):
        if ret_table[i][j] == 1:
            ret += 1
print(ret)


from collections import deque
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
visited = [[0] * m for _ in range(n)]


queue = deque()

graph = []
for i in range(n):
    line = list(map(int, si().split()))
    for j in range(m):
        if line[j] == 9:
            queue.append((i, j))
    graph.append(line)


# def bfs(q):
#     xd = [-1, 1, 0, 0]
#     yd = [0, 0, -1, 1]
#     while q:
#         x, y = q.popleft()
#         for idx in range(4):
#             r, c = x, y
#             nx, ny = xd[idx], yd[idx]
#             while True:
#                 if 0 > r or n <= r or 0 > c or c >= m:
#                     break
#                 visited[r][c] = 1
#                 if graph[r][c] == 3:
#                     nx, ny = -ny, -nx
#                 elif graph[r][c] == 4:
#                     nx, ny = ny, nx
#                 elif (graph[r][c] == 1 and nx == 0) or (graph[r][c] == 2 and ny == 0):
#                     break
#                 r += nx
#                 c += ny
#     return sum(sum(visited, []))


print(bfs(queue))