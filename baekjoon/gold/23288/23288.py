from collections import deque

def solution():
    answer = 0
    axis_arr = deque([6, 3, 1, 4])
    rest_arr = [5, 2]
    dir = 0
    N, M, K = map(int, input().split(" "))
    board = [list(map(int, input().split(" "))) for _ in range(N)]
    r, c = 0, 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    score = [[-1 for _ in range(M)] for _ in range(N)]

    def dfs(r, c, t):
        ret = [(r, c)]
        score[r][c] = 1
        for i in range(4):
            rr, cc = r + dx[i], c + dy[i]
            if rr < 0 or N <= rr or cc < 0 or M <= cc or score[rr][cc] != -1 or board[rr][cc] != t:
                continue
            else:
                score[rr][cc] = 1
            ret.extend(dfs(rr, cc, t))
        return ret

    for i in range(N):
        for j in range(M):
            if score[i][j] == -1:
                same = dfs(i, j, board[i][j])
                multi = len(same)
                for x, y in same:
                    score[x][y] = multi * board[i][j]

    def convert_axis(axis_arr, rest_arr):
        axis_arr, rest_arr = deque([axis_arr[0], rest_arr[0], axis_arr[2], rest_arr[1]]), [axis_arr[1], axis_arr[3]]
        return [axis_arr, rest_arr]

    def rotate(dir, axis_arr, rest_arr):
        dir = (dir + 1) % 4
        return [dir] + convert_axis(axis_arr, rest_arr)

    def reverse_rotate(dir, axis_arr, rest_arr):
        dir = (dir + 3) % 4
        return [dir] + convert_axis(axis_arr, rest_arr)

    def reverse_dir(dir):
        dir = (dir + 2) % 4
        return dir

    def go(dir, axis_arr: deque, r, c):
        if dir < 2:
            axis_arr.append(axis_arr.popleft())
        else:
            axis_arr.appendleft(axis_arr.pop())
        r, c = r + dx[dir], c + dy[dir]
        return dir, axis_arr, r, c

    r, c, dir = 0, 0, 0

    for i in range(K):
        rr, cc = r + dx[dir], c + dy[dir]
        if rr < 0 or N <= rr or cc < 0 or M <= cc:
            dir = reverse_dir(dir)
        dir, axis_arr, r, c = go(dir, axis_arr, r, c)
        if axis_arr[0] < board[r][c]:
            dir, axis_arr, rest_arr = reverse_rotate(dir, axis_arr, rest_arr)
        elif axis_arr[0] > board[r][c]:
            dir, axis_arr, rest_arr = rotate(dir, axis_arr, rest_arr)
        answer += score[r][c]
    return answer
print(solution())