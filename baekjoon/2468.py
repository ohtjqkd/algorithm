# input
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
# output: 5

# 단순구현?
N = int(input())
max_area_cnt = 1
def dfs(x, y, board):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    stack = []
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        board[x][y] = 0
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < N and 0 <= yy < N and board[xx][yy] > 0:
                stack.append((xx, yy))
    return

init_board = [list(map(int, input().split(" "))) for _ in range(N)]
S = sum(sum(init_board, []))
while S > 0:
    area_cnt = 0
    for i in range(N):
        for j in range(N):
            if init_board[i][j] > 0:
                init_board[i][j] -= 1
                S -= 1
    tmp_board = [[init_board[i][j] for j in range(N)] for i in range(N)]
    for x in range(N):
        for y in range(N):
            if tmp_board[x][y] > 0:
                area_cnt += 1
                dfs(x, y, tmp_board)
    max_area_cnt = max(max_area_cnt, area_cnt)
print(max_area_cnt)