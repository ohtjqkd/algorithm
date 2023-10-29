# input
# 6
# 1 1 1 1 1 1
# 2 2 6 2 2 3
# 2 2 5 2 2 3
# 2 2 2 4 6 3
# 0 0 0 0 0 6
# 0 0 0 0 0 9
# output
# 39
from heapq import heappop, heappush
from collections import deque

N = int(input())

result = 0
board = [list(map(int, input().split(' '))) for _ in range(N)]
size = 2
start_loc = (0, 0)
for i in range(N):
  for j in range(N):
    if board[i][j] == 9:
      start_loc = (i, j)
      board[i][j] = 0
      break

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
def bfs(x, y):
  visited = [[False for _ in range(N)] for _ in range(N)]
  q = deque([deque([(x, y)])])
  visited[x][y] = True
  time = 0
  while q:
    cand = []
    curr_depth = q.popleft()
    next_depth = deque()
    while curr_depth:
      x, y = curr_depth.popleft()
      for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
          continue
        if visited[nx][ny]:
          continue
        if board[nx][ny] > size:
          continue
        if board[nx][ny] < size and board[nx][ny] != 0:
          heappush(cand, (nx, ny))
        visited[nx][ny] = True
        next_depth.append((nx, ny))
    if cand:
      ret = heappop(cand)
      return ret[0], ret[1], time + 1
    if next_depth:
      q.append(next_depth)
    time += 1
  return None, None, None

x, y = start_loc[0], start_loc[1]
grow_cnt = size
while True:
  x, y, time = bfs(x, y)
  if time != None:
    result += time
  if x == None:
    print(result)
    break
  grow_cnt -= 1
  if grow_cnt == 0:
    size += 1
    grow_cnt = size
  board[x][y] = 0
