import string
import math
from itertools import permutations
from collections import defaultdict
tup = defaultdict(list)
def solution(m, n, board):
    answer = 0
    cand = set()
    global tup
    board = [list(b) for b in board]
    noBlock = ["*", "."]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] not in noBlock: cand.add(board[i][j])
            tup[board[i][j]].append((i, j))
    cand = sorted(list(cand))
    route = []
    answer = dfs(cand, board, route)
    print(answer)
    return answer

def dfs(cand, board, route):
    global tup
    if not cand:
        return route
    for i in range(len(cand)):
        if isRemovable(cand[i], board):
            one, two = tup.get(cand[i])
            route.append(cand[i])
            board[one[0]][one[1]], board[two[0]][two[1]] = ".", "."
            return dfs(cand[:i]+cand[i+1:], board, route)
    return "IMPOSSIBLE"

def isRemovable(block, board):
    global tup
    up, down = tup.get(block)
    chk = [".", block]
    if down[1] < up[1]:
        up, down = (up[0], down[1]), (down[0], up[1])
    if up[0] == down[0]:
        for i in range(up[1], down[1]+1):
            if board[up[0]][i] not in chk:
                return False
        return True

    if up[1] == down[1]:
        for i in range(up[0], down[0]+1):
            if board[i][up[1]] not in chk:
                return False
        return True

    right_down = True
    left_up = True
    for i in range(up[1], down[1]+1):
        if right_down and board[up[0]][i] not in chk:
            right_down = False
        if left_up and board[down[0]][i] not in chk:
            left_up = False
    
    for i in range(up[0], down[0]+1):
        if right_down and board[i][up[1]] not in chk:
            right_down = False
        if left_up and board[i][down[1]] not in chk:
            left_up = False
    return right_down or left_up

m, n, board = 3, 3, ["DBA", "C*A", "CDB"]
m, n, board = 2, 4, ["NRYN", "ARYA"]
m, n, board = 2, 2, ["AB", "BA"]
m, n, board = 4, 4, [".ZI.", "M.**", "MZU.", ".IU."]
solution(m, n, board)