R, C = map(int, input().split(" "))

t = 0
map_ = [list(input()) for _ in range(R)]
dist = [[float('inf') for _ in range(C)] for _ in range(R)]
f_end_node = set()

go = []

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for i in range(R):
    for j in range(C):
        if map_[i][j] == "*":
            f_end_node.add((i, j))
        if map_[i][j] == "S":
            go.append([(i, j)])
        if map_[i][j] == "D":
            dest = (i, j)
def expand(map_, end_nodes):
    next_end_nodes = set()
    while end_nodes:
        x, y = end_nodes.pop()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < R and 0 <= yy < C and map_[xx][yy] == ".":
                map_[xx][yy] = "*"
                next_end_nodes.add((xx,yy))
    return (map_, next_end_nodes)

while go:
    curr = go.pop()
    next_go = []
    map_, f_end_node = expand(map_, f_end_node)
    for x, y in curr:
        if dist[x][y] > t:
            dist[x][y] = t
        else:
            continue
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < R and 0 <= yy < C and (map_[xx][yy] == "." or dest == (xx, yy)):
                next_go.append((xx, yy))
    if len(next_go) > 0:
        go.append(next_go)
    t += 1

answer = dist[dest[0]][dest[1]]
if answer == float('inf'):
    print("KAKTUS")
else:
    print(answer)


# import sys
# from collections import deque

# # 도착 좌표
# end_x, end_y = 0, 0

# r, c = map(int, sys.stdin.readline().split())
# graph = [sys.stdin.readline().rstrip() for _ in range(r)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# # 물 전용 그래프 --> 도착칸과 벽칸을 제외하고 전부 0
# w_graph = [[0] * c for _ in range(r)]
# # 고슴도치 그래프 --> 벽칸과 물칸을 제외하고 전부 0
# s_graph = [[0] * c for _ in range(r)]

# w_queue = deque()
# s_queue = deque()

# for row in range(len(graph)):
#     for col in range(len(graph[row])):
#         if graph[row][col] == 'X':
#             w_graph[row][col] = -1
#             s_graph[row][col] = -1
#         # 출발칸인 경우
#         if graph[row][col] == 'S':
#             s_queue.append((row, col))
#         # 도착칸인 경우
#         elif graph[row][col] == 'D':
#             end_x, end_y = row, col
#             w_graph[row][col] = -1
#             s_graph[row][col] = -2
#         elif graph[row][col] == '*':
#             w_queue.append((row, col))
#             s_graph[row][col] = -1


# # 물
# def overflow():
#     while w_queue:
#         x, y = w_queue.popleft()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < r and 0 <= ny < c:
#                 if (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and w_graph[nx][ny] == 0:
#                     w_queue.append((nx, ny))
#                     w_graph[nx][ny] = w_graph[x][y] + 1


# # 고슴도치
# def bfs():
#     while s_queue:
#         x, y = s_queue.popleft()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < r and 0 <= ny < c:
#                 # 고슴도치가 진행할 수 있는 칸은 빈 곳 혹은 도착칸뿐이다.
#                 if (s_graph[nx][ny] == 0 or s_graph[nx][ny] == -2) and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
#                     # 물이 도달하는 시간보다 빨리 도착할 수 있는 곳으로 진행한다.
#                     if s_graph[x][y] + 1 < w_graph[nx][ny] or w_graph[nx][ny] == -1:
#                         s_graph[nx][ny] = s_graph[x][y] + 1
#                         s_queue.append((nx, ny))


# overflow()
# bfs()

# if s_graph[end_x][end_y] == -2:
#     print("KAKTUS")
# else:
#     print(s_graph[end_x][end_y])