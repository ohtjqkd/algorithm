from collections import defaultdict
N = int(input())
result = []
score = 0
like_pair = []
like_pair_otherside = defaultdict(list)
for _ in range(N ** 2):
    tmp = list(map(lambda x: int(x) - 1, input().split(" ")))
    like_pair.append([tmp[0], tmp[1:]])
    for i in tmp[1:]:
        like_pair_otherside[i].append(tmp[0])
check_board = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N ** 2)]
empty_board = [[4 for _ in range(N)] for _ in range(N)]
for i in range(N):
    empty_board[i][0] = 3
    empty_board[0][i] = 3
    empty_board[N - 1][i] = 3
    empty_board[i][N - 1] = 3
empty_board[0][0], empty_board[0][N - 1], empty_board[N - 1][0], empty_board[N - 1][N - 1] = 2, 2, 2, 2

def find_max_seat(check_board, empty_board):
    MAX = -1
    ret = []
    for i in range(N):
        for j in range(N):
            if empty_board[i][j] < 0:
                continue
            if check_board[i][j] > MAX:
                ret = [(i, j)]
                MAX = check_board[i][j]
            elif check_board[i][j] == MAX:
                ret.append((i, j))
    return ret

def find_max_empty_seat(empty_board, locs):
    MAX = -1
    ret = None
    for x, y in locs:
        if empty_board[x][y] > MAX:
            ret = (x, y)
            MAX = empty_board[x][y]
    return ret

def decrease_empty(empty_board, r, c):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    empty_board[r][c] = -1
    for i in range(4):
        xx, yy = r + dx[i], c + dy[i]
        if 0 <= xx < N and 0 <= yy < N:
            empty_board[xx][yy] -= 1
    return empty_board

def increase_like(check_board, pair, r, c):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for j in pair:
        for i in range(4):
            xx, yy = r + dx[i], c + dy[i]
            if 0 <= xx < N and 0 <= yy < N:
                check_board[j][xx][yy] += 1
    return check_board


for n, like_list in like_pair:
    r, c = find_max_empty_seat(empty_board, find_max_seat(check_board[n], empty_board))
    result.append([n, r, c])
    empty_board = decrease_empty(empty_board, r, c)
    check_board = increase_like(check_board, like_pair_otherside[n], r, c)
for n, r, c in result:
    if check_board[n][r][c] == 0:
        continue
    else:
        score += 10 ** (check_board[n][r][c] - 1)
print(score)