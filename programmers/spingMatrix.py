def solution(rows, columns, queries):
    answer = []
    board = [[columns*j+i for i in range(1, columns+1)] for j in range(rows)]
    for q in queries:
        answer.append(spin(board, q))
    return answer

def spin(board, query):
    printb(board)
    print()
    min_v = float('inf')
    x1, y1, x2, y2 = query
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    tmp = board[x1][y1]
    for y in range(y1+1, y2+1):
        min_v = min(min_v, tmp)
        tmp1 = board[x1][y]
        board[x1][y] = tmp
        tmp = tmp1
        # board[x][y1], tmp = tmp, board[x][y1]
    for x in range(x1+1, x2+1):
        min_v = min(min_v, tmp)
        tmp1 = board[x][y2]
        board[x][y2] = tmp
        tmp = tmp1
        # board[x2][y], tmp = tmp, board[x2][y]
    for y in range(y2-1, y1-1, -1):
        min_v = min(min_v, tmp)
        board[x2][y], tmp = tmp, board[x2][y]
    for x in range(x2-1, x1-1, -1):
        min_v = min(min_v, tmp)
        board[x][y1], tmp = tmp, board[x][y1]
    return min_v

def printb(board):
    for b in board:
        print(b)
rows, columns, queries = 6,	6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


print(solution(rows, columns, queries))