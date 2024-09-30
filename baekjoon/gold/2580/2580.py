import copy

sample = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def sudoku(arr, locations):
    if len(locations) == 0:
        return arr
    else:
        x, y = locations[0]
        reserve = sample-set(arr[x])-{arr[0][y], arr[1][y], arr[2][y], arr[3][y], arr[4][y], arr[5][y], arr[6][y], arr[7][y], arr[8][y]} \
            -set(arr[(x//3)*3][(y//3)*3:(y//3)*3+3])-set(arr[(x//3)*3+1][(y//3)*3:(y//3)*3+3])-set(arr[(x//3)*3+2][(y//3)*3:(y//3)*3+3])
        for i in reserve:
            arr[x][y] = i
            tmp_arr = sudoku(arr, locations[1:])
            if tmp_arr:
                return tmp_arr
            arr[x][y] = 0


# def check(arr):
#     for i in range(9):
#         print(arr[i*9:i*9+9])
#         if len(arr[i*9:i*9+9]) != len(set(arr[i*9:i*9+9])):
#             return False
#     return True

    # xx, yy = [-1, 0, 1], [-1, 0, 1]

    # for x in [1, 4, 7]:
    #     for y in [1, 4, 7]:
    #         ns = []
    #         for dx in xx:
    #             for dy in yy:
    #                 ns.append(arr[x+dx][y+dy])
    #         if len(ns) != len(set(ns)):
    #             return False


# board1 = [[0] * 9 for _ in range(9)]
# board2 = [[0] * 9 for _ in range(9)]
# board3 = [0] * 81
locations = []
board1 = []
for i in range(9):
    input_v = list(map(int, input().split()))
    board1.append(input_v)
for i in range(9):
    for j in range(9):
        # board2[i][j] = board1[j][i]
        # board3[i*9+j] = board1[i][j]
        if board1[i][j] == 0:
            locations.append((i, j))


result = sudoku(board1, locations)
for r in range(9):
    for i in range(9):
        if i == 8 and r == 8:
            print(result[r][i], end='')
        elif i == 8:
            print(result[r][i])
        else:
            print(result[r][i], end=' ')