from collections import defaultdict
import heapq as hq
maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]


def solution(maps):
    answer = 1
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    heap = []
    nodes = defaultdict(list)
    row, col = len(maps), len(maps[0])
    distances = [[float('inf') for _ in range(col)] for _ in range(row)]
    distances[0][0] = 1
    hq.heappush(heap, [1, (0, 0)])
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 1:
                for k in range(4):
                    xx, yy = i+dx[k], j+dy[k]
                    if 0 <= xx < row and 0 <= yy < col and maps[xx][yy]:
                        nodes[(i, j)].append((xx, yy))
    while heap:
        now_distance, now_loc = hq.heappop(heap)

        for next_loc in nodes[now_loc]:
            next_x, next_y = next_loc
            if distances[next_x][next_y] > now_distance + 1:
                distances[next_x][next_y] = now_distance + 1
                hq.heappush(heap, [distances[next_x][next_y], next_loc])
    print(distances)
    return distances[-1][-1] if distances[-1][-1] != float('inf') else -1


print(solution(maps))
