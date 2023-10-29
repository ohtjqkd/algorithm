# input
# 3 5
# 42101
# 22100
# 22101
# output
# 9

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
ans = 0
for i in range(n):
  for j in range(m):
    a = board[i][j]
    d = 0
    while i + d < n and j + d < m:
      if board[i + d][j] == a and board[i][j + d] == a and board[i + d][j + d] == a:
        ans = max(ans, (d + 1) ** 2)
      d += 1 
print(ans)