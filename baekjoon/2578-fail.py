board = [list(map(int, input().split(" "))) for _ in range(5)]
mapping = {}
bingo = 0
row, col, diag = [5 for _ in range(5)], [5 for _ in range(5)], [5 for _ in range(2)]
for i in range(5):
    for j in range(5):
        mapping[board[i][j]] = (i, j)
is_bingo = False
for i in range(5):
    nums = list(map(int, input().split(" ")))
    for j in range(len(nums)):
        r, c = mapping[nums[j]]
        # print(r, c)
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

        if row[r] <= 0:
            bingo += 1
        if col[c] <= 0:
            bingo += 1
        # print(row, col, diag, r, c)
        if bingo == 3:
            print(i*5+j+1)
            is_bingo = True
            break
    if is_bingo:
        break
# print(mapping)