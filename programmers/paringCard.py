from collections import defaultdict
from itertools import permutations
from copy import deepcopy
board, r, c = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0
# board, r, c = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1

location = defaultdict(list)


def getNextPoint(board, now):
    pass


def prevToNext(board, start, target):
    ret = 0
    if start == target:
        return ret
    visited = [[0 if i != start[0] or j != start[1]
                else 1 for j in range(4)] for i in range(4)]
    need_visit = [[start]]
    print(start, target)
    while need_visit:
        print(need_visit)
        tmp = []
        nodes = need_visit.pop()
        for node in nodes:
            if node == target:
                print(ret)
                return ret
            x, y = node
            visited[x][y] = 1
            for i in range(x-1, -1, -1):
                if visited[i][y]:
                    continue
                if board[i][y] != 0 or i == 0:
                    tmp.append((i, y))
                    break
                if i == x-1:
                    tmp.append((i, y))
            for i in range(y-1, -1, -1):
                if visited[x][i]:
                    continue
                if board[x][i] != 0 or i == 0:
                    tmp.append((x, i))
                    break
                if i == x-1:
                    tmp.append((x, i))
            for i in range(x+1, 4):
                if visited[i][y]:
                    continue
                if board[i][y] != 0 or i == 3:
                    tmp.append((i, y))
                    break
                if i == x+1:
                    tmp.append((i, y))
            for i in range(y+1, 4):
                if visited[x][i]:
                    continue
                if board[x][i] != 0 or i == 3:
                    tmp.append((x, i))
                    break
                if i == y+1:
                    tmp.append((x, i))
        ret += 1
        need_visit.append(tmp)
    return ret


def recursive(board, order, target, now, moveCnt):
    global location
    if len(order) == target:
        return moveCnt

    location_1, location_2 = location[order[target]]

    n_to_o = prevToNext(board, now, location_1)
    o_to_t = prevToNext(board, location_1, location_2)
    n_to_t = prevToNext(board, now, location_2)
    t_to_o = prevToNext(board, location_2, location_1)
    goLastTwo = n_to_o + o_to_t
    goLastOne = n_to_t + t_to_o

    x1, y1 = location_1
    x2, y2 = location_2
    tmp1, tmp2 = board[x1][y1], board[x2][y2]
    board[x1][y1], board[x2][y2] = 0, 0
    one = recursive(board, order, target+1, location_1, moveCnt+goLastOne)
    two = recursive(board, order, target+1,  location_2, moveCnt+goLastTwo)
    board[x1][y1], board[x2][y2] = tmp1, tmp2
    o_d = one
    t_d = two
    return min(o_d, t_d)  # , route


def solution(board, r, c):
    global location
    for rowIdx, row in enumerate(board):
        for colIdx, col in enumerate(row):
            location[col].append((rowIdx, colIdx))
    cards = location.keys()
    cards = [c for c in cards if c != 0]
    perm = list(permutations(cards))
    movement = float('inf')
    for order in perm:
        order = list(order)
        print(order)
        move = recursive(board, order, 0, (r, c), 0)
        movement = min(movement, move)
    return movement + 2*len(cards)


print(solution(board, r, c))
