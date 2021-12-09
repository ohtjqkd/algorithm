# input
# 1 2 4 4
# 2 3 5 7
# 3 1 6 5
# 7 3 8 6
# output: 26
from my_module.modules import print_board
papers = [list(map(int, input().split(" "))) for _ in range(4)]
board = [[0 for _ in range(100)] for _ in range(100)]
for x1, y1, x2, y2 in papers:
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1
print(sum(sum(board, [])))