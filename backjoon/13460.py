import sys
input = sys.stdin.readline
N, M = map(int, input().split())
print(N, M)
board = [list(input().strip()) for _ in range(N)]
print(board)
loc = dict()
loc_r, loc_b = None, None

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            loc_r = (i, j)
            loc["R"] = (i, j)
        elif board[i][j] == "B":
            loc_b = (i, j)
            loc["B"] = (i, j)
        elif board[i][j] == "O":
            loc["O"] = (i, j)
print(loc)
def dfs(loc_r, loc_b, board, tilt):
    move_r, move_b = False, False
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(4):
        nxt_r, nxt_b = board[loc_r[0]+dx[i]][loc_r[1]+dy[i]], board[loc_b[0]+dx[i]][loc_b[1]+dy[i]]
        if nxt_r != "." and nxt_b != ".":
            
    pass
