import sys
import math
input = sys.stdin.readline
visited = [0] * (123456*2+1)
visited[0], visited[1] = 1, 1
for i in range(2, int(math.sqrt(123456*2))+1):
    for j in range(2, 123456*2//i+1):
        visited[i*j] = 1

while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if visited[i] == 0:
            count += 1
    print(count)
