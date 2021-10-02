import sys
input = sys.stdin.readline
n = int(input())
locations = []
for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))
# 내장함수
locations.sort()

for x, y in locations:
    print(x, y)
