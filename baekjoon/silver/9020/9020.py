import math
visited = [0] * 10001
visited[0], visited[1] = 1, 1
for i in range(2, 101):
    for j in range(2, 10000//i+1):
        visited[i*j] = 1
for _ in range(int(input())):
    n = int(input())
    half = n//2
    for i in range(half, 1, -1):
        if visited[i] == 0 and visited[n-i] == 0:
            print(i, n-i)
            break
