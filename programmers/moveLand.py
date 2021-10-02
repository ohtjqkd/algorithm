from collections import defaultdict
import heapq as hq


land, height = [[1, 4, 8, 10], [5, 5, 5, 5],
                [10, 10, 10, 10], [10, 10, 10, 20]], 3

land, height = [[10, 11, 10, 11], [2, 21, 20, 10],
                [1, 20, 21, 11], [2, 1, 2, 1]], 1

# land, height = [[(j*600 + i*2) for i in range(300)] for j in range(300)], 1
# land, height = [[]]


def pb(arr):
    for a in arr:
        print(a)


def makeArea(area, land, x, y, d, land_number):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    # visited = [[0 for _ in range(len(land))] for _ in range(len(land))]
    need_visit = [(x, y)]
    while need_visit:
        now_node = need_visit.pop()
        x, y = now_node
        now_height, area[x][y] = land[x][y], land_number
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < len(land) and 0 <= yy < len(land) and not area[xx][yy]:
                if abs(now_height-land[xx][yy]) <= d:
                    need_visit.append((xx, yy))
    return


def getParent(parents, node):
    if parents[node] == node:
        return node
    return getParent(parents, parents[node])


def solution(land, height):
    answer = 0
    area = [[0 for _ in range(len(land))] for _ in range(len(land))]
    connected = defaultdict(int)
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    heap = []
    value = 1
    for i in range(len(land)):
        for j in range(len(land)):
            if area[i][j] == 0:
                makeArea(area, land, i, j, height, value)
                value += 1

    for i in range(len(land)):
        for j in range(len(land)):
            now_area_number = area[i][j]
            for k in range(4):
                xx, yy = i+dx[k], j+dy[k]
                if 0 <= xx < len(land) and 0 <= yy < len(land):
                    if now_area_number != area[xx][yy]:
                        hq.heappush(
                            heap, [abs(land[i][j]-land[xx][yy]), (now_area_number, area[xx][yy])])
    parents = [i for i in range(value)]
    # parents = dict()
    # for i in range(1, value):
    #     parents[i] = i
    while heap:
        value, areas = hq.heappop(heap)
        area1, area2 = areas
        # join방법 개선
        # following case, it can be considered, 이방법에서는 다음과 같은 경우를 계산할 수 없음
        # ex: 최소비용 (1, 2)가 뽑혔을 때 1, 3이 연결되어 있고, 2, 4가 연결되어 있으면 패스함
        parent_1, parent_2 = getParent(
            parents, area1), getParent(parents, area2)
        if parent_1 != parent_2:
            answer += value
            if parent_1 > parent_2:
                parents[parent_2] = parent_1
            else:
                parents[parent_1] = parent_2
            # print(parents)
        # pb(area)
        # print(parents)
        # print()
    return answer


print(solution(land, height))
