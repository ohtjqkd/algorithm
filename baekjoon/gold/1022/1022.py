# input
# -3 -3 2 0
# output
# 37 36 35 34
# 38 17 16 15
# 39 18  5  4
# 40 19  6  1
# 41 20  7  8
# 42 21 22 23

r1, c1, r2, c2 = map(int, input().split(' '))

board = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
max_value = 0
for i in range(r2 - r1 + 1):
  for j in range(c2 - c1 + 1):
    x, y = i + r1, j + c1
    level = max(abs(x), abs(y))
    start_level_loc = (level - 1, level)
    start_value = (level * 2 - 1) ** 2 + 1
    if y == level and x <= start_level_loc[0]:
      index = abs(start_level_loc[0] - x)
    elif -x == level:
      index = abs(start_level_loc[1] - y) + level * 2 - 1
    elif y == -level:
      index = abs(level + x) + level * 4 - 1
    else:
      index = y + level + level * 6 - 1
    board[i][j] = start_value + index
    max_value = max(max_value, board[i][j])
    
max_exp = len(str(max_value))
for i in range(len(board)):
  for j in range(len(board[0])):
    num_str = str(board[i][j])
    board[i][j] = " " * (max_exp - len(num_str)) + num_str
    
for b in board:
  print(' '.join(b))

