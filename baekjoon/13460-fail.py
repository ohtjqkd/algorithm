# input
# 5 5
# #####
# #..B#
# #.#.#
# #RO.#
# #####
# output
# 1
import sys
from my_module.modules import print_board
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            loc_r = [i, j]
            board[i][j] = "."
        if board[i][j] == "B":
            loc_b = [i, j]
            board[i][j] = "."
memo = {}

def move(board, loc, dx, dy):
    cnt = 0
    x, y = loc
    while 0 <= x+dx < len(board) and 0 <= y+dy < len(board[0]):
        if board[x+dx][y+dy] == "#":
            return [[x, y], cnt]
        if board[x+dx][y+dy] == "O":
            return True
        x += dx
        y += dy
        cnt += 1
    return [[x, y], cnt]

def dfs(loc_r, loc_b, board, tilt, cnt):
    ret = float('inf')
    if cnt >= 10:
        return float('inf')
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    for i in range(4):
        if tilt == i or (tilt+2) % 4 == i:
            continue
        m_b = move(board, loc_b, dx[i], dy[i])
        m_r = move(board, loc_r, dx[i], dy[i])
        if m_r == True and m_b != True:
            return cnt+1
        if m_b == True:
            return float('inf')
        if m_r[0] == m_b[0]:
            if m_r[1] > m_b[1]:
                m_r[0] = (m_r[0][0]-dx[i], m_r[0][1]-dy[i])
            else:
                m_b[0] = (m_b[0][0]-dx[i], m_b[0][1]-dy[i])
        ret = min(ret, dfs(m_r[0], m_b[0], board, i, cnt+1))
    return ret

ret = float('inf')
for i in range(4):
    ret = min(ret, dfs(loc_r, loc_b, board, i, 0))
if ret == float('inf'):
    print(-1)
else:
    print(ret)