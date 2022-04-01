# 문자열 제거
# 몰라

import sys

input = sys.stdin.readline

S = input()
M = int(input())
A = []
for i in range(M):
    a, n = input().split(" ")
    A.append((int(n), a))
print(sorted(A))
