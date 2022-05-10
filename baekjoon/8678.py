import sys

input = sys.stdin.readline

z = int(input())

for _ in range(z):
    a, b = map(int, input().rstrip().split(" "))
    if b % a == 0:
        print("TAK")
    else:
        print("NIE")