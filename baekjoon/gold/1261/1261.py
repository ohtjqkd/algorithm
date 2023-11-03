# 미로는 N*M, (1<= N,M <= 100)
# 빈방 혹은 벽으로 이루어져 있음
# 벽은 부수지 않으면 이동할 수 없다.
# 운영진은 여러명이며 항상 모두 같은 방에 있어야 한다.
# 이동은 상하좌우 인접 방으로 가능하며 벽을 부수면 이동이 가능하다.
# (0, 0)에서 (N, M)까지 가려면 벽을 최소 몇 개 부서어야 하는지 구하여라
# * 이동 횟수와는 상관이 없는거 같다.

# input
# 6 6
# 001111
# 010000
# 001111
# 110001
# 011010
# 100010
import heapq
N, M = map(int, input().split())
maze = [list(input()) for _ in range(M)]
distances = [[float('inf') for _ in range(N)] for _ in range(M)]
heap = []
distances[0][0] = 0
heapq.heappush(heap, (0, 0, 0))
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
while heap:
    w, x, y = heapq.heappop(heap)
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx == M-1 and yy == N-1:
            print(w)
            exit()
        if 0 <= xx < M and 0 <= yy < N:
            if maze[xx][yy] == '0' and distances[xx][yy] > w:
                heapq.heappush(heap, (w, xx, yy))
                distances[xx][yy] = w
            elif maze[xx][yy] == '1' and distances[xx][yy] > w+1:
                heapq.heappush(heap, (w+1, xx, yy))
                distances[xx][yy] = w+1
print(distances[-1][-1])