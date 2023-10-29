# input
# 6 7 3
# .......
# ...O...
# ....O..
# .......
# OO.....
# OO.....
# output
# OOO.OOO
# OO...OO
# OOO...O
# ..OO.OO
# ...OOOO
# ...OOOO

R, C, N = map(int, input().split())

grid = [list(input()) for _ in range(R)]
reverse_grid = [list('O' * C) for _ in range(R)]
full_grid = [list('O' * C) for _ in range(R)]

for i in range(R):
  for j in range(C):
    if grid[i][j] == '':
      reverse_grid[i][j] = '.'
      if i - 1 >= 0:
        reverse_grid[i - 1][j] = '.'
      if i + 1 < R:
        reverse_grid[i + 1][j] = '.'
      if j - 1 >= 0:
        reverse_grid[i][j - 1] = '.'
      if j + 1 < C:
        reverse_grid[i][j + 1] = '.'

def print_grid(grid):
  for g in grid:
    print(''.join(g))

match N % 4:
  case 0:
    print_grid(full_grid)
  case 1:
    print_grid(grid)
  case 2:
    print_grid(full_grid)
  case 3:
    print_grid(reverse_grid)
