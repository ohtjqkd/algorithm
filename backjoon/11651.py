import sys
input = sys.stdin.readline
n = int(input())
locations = []
for _ in range(n):
    x, y = map(int, input().split())
    locations.append((y, x))

locations.sort()

for y, x in locations:
    print(x, y)
