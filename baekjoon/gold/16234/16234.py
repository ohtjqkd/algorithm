# input
# 2 20 50
# 50 30
# 20 40
# output
# 1

N, L, R = map(int, input().split(' '))

board = [list(map(int, input().split(' '))) for _ in range(N)]

# while True:
#   is_changed = False
#   visited = [[False] * N for _ in range(N)]
#   for i in range(N):
#     for j in range(N):
#       if visited[i][j]:
#         continue
#       visited[i][j] = True
#       stack = [(i, j)]
#       union = [(i, j)]
#       while stack:
#         x, y = stack.pop()
#         for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
#           nx, ny = x + dx, y + dy
#           if nx < 0 or nx >= N or ny < 0 or ny >= N:
#             continue
#           if visited[nx][ny]:
#             continue
#           if L <= abs(board[x][y] - board[nx][ny]) <= R:
#             visited[nx][ny] = True
#             stack.append((nx, ny))
#             union.append((nx, ny))
#       if len(union) > 1:
#         is_changed = True
#         avg = sum(board[x][y] for x, y in union) // len(union)
#         for x, y in union:
#           board[x][y] = avg
#   if not is_changed:
#     break

def dfs(x, y):
  global next_board
  
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
day = 0
while True:
  is_changed = False
  next_board = [[-1] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if next_board[i][j] == -1:
        continue
      for k in range(4):
        x, y = i + dx[k], j + dy[k]
        