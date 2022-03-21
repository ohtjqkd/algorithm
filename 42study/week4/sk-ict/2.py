from collections import deque
import math
def solution(n, clockwise)->list:
    ret = [[0 for _ in range(n)] for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    step = 1 if clockwise else 3
    start_idx = 0 if clockwise else 1
    q = deque([(0, 0, (0+start_idx)%4), (0, n-1, (1+start_idx)%4), (n-1, n-1, (2+start_idx)%4), (n-1, 0,(3+start_idx)%4)])
    M = math.ceil(n**2/4)
    n -= 1
    for x,y,_ in q:
        ret[x][y] = 1
    middle = (n//2, n//2 + n%2)
    for i in middle:
        for j in middle:
            ret[i][j] = M
    while q:
        x, y, d = q.popleft()
        if ret[x][y] == M:
            continue
        xx, yy = x+dx[d], y+dy[d]
        if ret[xx][yy] != 0:
            d = (d + step) % 4
            xx, yy = x+dx[d], y+dy[d]
        ret[xx][yy] = ret[x][y] + 1
        q.append((xx,yy,d))
        for r in ret:
            print(r)

    return ret

T = [[5,True, [[1,2,3,4,1],[4,5,6,5,2],[3,6,7,6,3],[2,5,6,5,4],[1,4,3,2,1]]],
    [6, False, [[1,5,4,3,2,1],[2,6,8,7,6,5],[3,7,9,9,8,4],[4,8,9,9,7,3],[5,6,7,8,6,2],[1,2,3,4,5,1]]],
    [9, False, [[1,8,7,6,5,4,3,2,1],[2,9,14,13,12,11,10,9,8],[3,10,15,18,17,16,15,14,7],[4,11,16,19,20,19,18,13,6],[5,12,17,20,21,20,17,12,5],[6,13,18,19,20,19,16,11,4],[7,14,15,16,17,18,15,10,3],[8,9,10,11,12,13,14,9,2],[1,2,3,4,5,6,7,8,1]]]]

for t in T:
    for r in t[2]:
        print(r)
    print(t[2] == solution(t[0], t[1]))