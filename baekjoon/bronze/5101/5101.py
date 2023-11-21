import sys

input = sys.stdin.readline

while True:
    s, d, n = map(int, input().rstrip().split(" "))
    if s == 0 and d == 0 and n == 0:
        break
    if (n - s) % d == 0 and (n - s) // d >= 0:
        print((n - s) // d + 1)
    else:
        print("X")