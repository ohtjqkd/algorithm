def solution(arr, n):
    cnt = 0
    areas = []
    def count_area(x, y):
        ret = 1
        arr[x][y] = 0
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if 0 <= xx < n and 0 <= yy <n and arr[xx][yy] == 1:
                ret += count_area(xx, yy)
        return ret
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
                areas.append(count_area(i, j))
    
    return [cnt] + sorted(areas)


n = int(input())
arr = [list(map(int, list(input()))) for _ in range(n)]
print(solution(arr, n))