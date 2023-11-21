# input
# 11 12 2 24 10
# 16 1 13 3 25
# 6 20 5 21 17
# 19 4 8 14 9
# 22 15 7 23 18
# 5 10 7 16 2
# 4 22 8 17 13
# 3 18 1 6 25
# 12 19 23 14 21
# 11 24 9 20 15
# output
# 15

board = [list(map(int, input().split(" "))) for _ in range(5)]
mapping = {}
bingo = 0
row, col, diag = [5 for _ in range(5)], [5 for _ in range(5)], [5 for _ in range(2)]
for i in range(5):
    for j in range(5):
        mapping[board[i][j]] = (i, j)
mc = []
for _ in range(5):
    mc.extend(list(map(int, input().split(" "))))
for i in range(len(mc)):
    r, c = mapping[mc[i]]
    row[r] -= 1
    col[c] -= 1
    if r == c and r + c == 4:
        diag[0] -= 1
        diag[1] -= 1
        if diag[0] <= 0:
            bingo += 1
        if diag[1] <= 0:
            bingo += 1
    elif r == c:
        diag[0] -= 1
        if diag[0] <= 0:
            bingo += 1
    elif r + c == 4:
        diag[1] -= 1
        if diag[1] <= 0:
            bingo += 1
    if row[r] == 0:
        bingo += 1
    if col[c] == 0:
        bingo += 1
    if bingo >= 3:
        print(i+1)
        break