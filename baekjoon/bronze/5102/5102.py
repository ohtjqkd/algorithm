import sys

input = sys.stdin.readline

while True:
    d1, d2 = map(int, input().rstrip().split(" "))
    if d1 == 0 and d2 == 0:
        break
    if d1 - d2 < 2:
        print(0, 0)
    else:
        a = (d1 - d2) // 2 - (d1 - d2 - 2) % 2
        b = (d1 - d2 - 2) % 2
        print(a, b)