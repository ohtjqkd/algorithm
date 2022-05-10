import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().rstrip().split(" "))
    fund = 0
    if N == 0 and M == 0:
        break
    div = M // N
    A = map(int, input().rstrip().split(" "))
    for a in A:
        fund += min(div, a)
    print(fund)