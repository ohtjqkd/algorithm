from my_module.modules import get_str_list
def solution(places):
    answer = []
    def dfs(x, y, dist, idx, visited):
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        ret = True
        if 2 >= dist > 0 and places[idx][x][y] == 'P':
            return False
        if dist > 2 or places[idx][x][y] == 'X':
            return True
        for i in range(4):
            visited[(x, y)] = False
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < 5 and 0 <= yy < 5 and visited.get((xx, yy), True):
                ret = (ret and dfs(xx, yy, dist + 1, idx, visited))
            visited[(x, y)] = True
        return ret
    for i in range(len(places)):
        curr = places[i]
        check = True
        for j in range(5):
            for k in range(5):
                if curr[j][k] == 'P':
                    check = dfs(j, k, 0, i, {})
            if not check:
                break
        if not check:
            answer.append(0)
        else:
            answer.append(1)
    return answer
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
places = [
    [
        "XXPXX",
        "XPXPX",
        "POPOP",
        "XP"
    ]
]
places = get_str_list()
solution(places)