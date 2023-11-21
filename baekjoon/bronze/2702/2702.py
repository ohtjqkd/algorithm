# input
# 3
# 5 10
# 7 23
# 42 56
# output
# 10 5
# 161 1
# 168 14

import sys
input = sys.stdin.readline
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

for _ in range(int(input())):
    a, b = map(int, input().split(" "))
    g = gcd(a, b)
    print(a*b//g, g)
