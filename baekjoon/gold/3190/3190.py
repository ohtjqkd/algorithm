# input
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
# output: 9

from collections import deque

def solution():
    N = int(input())
    K = int(input())
    apple = {input(): True for _ in range(K)}
    board = [[0 for _ in range(N)] for _ in range(N)]
    head, dir, time = [1, 1], 0, 0
    board[0][0] = 1

    L = int(input())
    turn_time = ['' for _ in range(10001)]
    for _ in range(L):
        T, D = input().split(" ")
        turn_time[int(T)] = D
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    snake = deque([[1,1]])

    while True:
        n_x, n_y = [head[0]+dx[dir], head[1]+dy[dir]]
        is_apple = apple.get(f'{n_x} {n_y}', False)
        if not (1 <= n_x <= N) or not (1 <= n_y <= N) or board[n_x-1][n_y-1] == 1:
            return time
        snake.append([n_x, n_y])
        board[n_x-1][n_y-1] = 1
        if not is_apple:
            tail = snake.popleft()
            board[tail[0]-1][tail[1]-1] = 0
        else:
            apple[f'{n_x} {n_y}'] = False
        head = [n_x, n_y]
        time += 1
        if turn_time[time] == "L":
            dir = (dir-1)%4
        elif turn_time[time] == "D":
            dir = (dir+1)%4
print(solution()+1)

