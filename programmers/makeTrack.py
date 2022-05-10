def solution(board):
    N = len(board)
    cost_table = [[[float('inf'), float('inf'), float('inf'), float('inf')] if board[i][j] == 0 else [float('-inf'), float('-inf'), float('-inf'), float('-inf')] for j in range(len(board))] for i in range(len(board))]
    cost_table[0][0] = [0, 0, 0, 0]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    stack = [[0, 0, i] for i in range(4)]
    while stack:
        x, y, prev_dir = stack.pop()
        for i in range(4):
            cost = 100
            if abs(prev_dir - i) == 2:
                continue
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < N and 0 <= yy < N:
                if i != prev_dir:
                    cost = 600
                if cost_table[x][y][prev_dir] + cost < cost_table[xx][yy][i]:
                    cost_table[xx][yy][i] = cost_table[x][y][prev_dir] + cost
                    stack.append([xx, yy, i])
    return min(cost_table[N-1][N-1])

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))