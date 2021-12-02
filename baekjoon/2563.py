# input
# 3
# 3 7
# 15 7
# 5 2
# output: 260
from my_module.modules import print_board
board = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input())):
    r_s, c_s = map(int, input().split(" "))
    for i in range(r_s, r_s+10):
        for j in range(c_s, c_s+10):
            board[i][j] = 1
print(sum(sum(board, [])))

# dp로도 풀 수 있을거 같은데...흠...



