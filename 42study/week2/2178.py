from heapq import heappop, heappush
N, M = map(int, input().split(" "))
distances = [[float('inf') for _ in range(M)] for _ in range(N)]
miro = [list(map(int, list(input()))) for _ in range(N)]
distances[0][0] = 0
heap = []
heappush(heap, (0, (0, 0)))
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
while heap:
    w, (r, c) = heappop(heap)
    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]
        if 0 <= rr < N and 0 <= cc < M and miro[rr][cc] != 0 and distances[rr][cc] > w+1:
            distances[rr][cc] = w+1
            heappush(heap, (w+1, (rr, cc)))
print(distances[N-1][M-1]+1)