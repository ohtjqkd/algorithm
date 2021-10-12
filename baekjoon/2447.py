n = int(input())
start = [['']*n for _ in range(n)]
board = [[' '] * n for _ in range(n)]


def print_star(x, y, n):
    if n == 1:
        board[x][y] = '*'
        return
    div = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                print_star(x+i*div, y+j*div, div)


print_star(0, 0, n)
for b in board:
    print(''.join(b))
