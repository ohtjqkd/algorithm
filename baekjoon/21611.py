# input
# 7 1
# 0 0 0 0 0 0 0
# 3 2 1 3 2 3 0
# 2 1 2 1 2 1 0
# 2 1 1 0 2 1 1
# 3 3 2 3 2 1 2
# 3 3 3 1 3 3 2
# 2 3 2 2 3 2 3
# 2 2
# output
# 28

N, M = map(int, input().split(" "))
init_board = [list(map(int, input().split(" "))) for _ in range(N)]

shark = (N//2, N//2)

plat_board = [0, init_board[shark[0]][shark[1]-1], init_board[shark[0]-1][shark[1]-1], init_board[shark[0]-1][shark[1]]]

print(plat_board)

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

