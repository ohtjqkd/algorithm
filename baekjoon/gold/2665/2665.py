# input
# 8
# 11100110
# 11010010
# 10011010
# 11101100
# 01000111
# 00110001
# 11011000
# 11000111
# output
# 2
import heapq
row = int(input())
board = [list(input()) for _ in range(row)]
distances = [[float('inf') for _ in range(row)] for _ in range(row)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
heap = []
distances[0][0] = 0
heapq.heappush(heap, (0, 0, 0))
while heap:
    w, x, y = heapq.heappop(heap)
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0 <= xx < row and 0 <= yy < row:
            if board[xx][yy] == '0' and distances[xx][yy] > w+1:
                heapq.heappush(heap, (w+1, xx, yy))
                distances[xx][yy] = w+1
            elif board[xx][yy] == '1' and distances[xx][yy] > w:
                heapq.heappush(heap, (w, xx, yy))
                distances[xx][yy] = w
print(distances[-1][-1])

