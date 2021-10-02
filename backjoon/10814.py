import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    x, y = list(input().split())
    li.append((int(x), y))

li.sort(key=lambda x: x[0])
for x, y in li:
    print(x, y)
