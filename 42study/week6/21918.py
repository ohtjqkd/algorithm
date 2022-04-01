# 전구
# 비트연산을 사용하고 싶다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
B = input().replace(" ", "")
B = int(B, 2)

# 더 생각해보기# print(B)
# print(bin(0b1011 ^ 0b1000))
# B = B + 2 ** (N + 1)
for i in range(M):
    c, a, b = map(int, input().split(" "))
    if c == 1:
        if b == 0:
            B = B & ~(2 ** (N - a))
        if b == 1:
            B = B | (2 ** (N - a))
    if c == 2:
        B = ~B ^ ~((2 ** (b - a + 1)) - 1 << (N - b))
    if c == 3:
        B = B - (B & (2 ** (b - a + 1)) - 1 << (N - b))
    if c == 4:
        B = B + ~(B | ~(2 ** (b - a + 1) - 1 << (N - b)))
        # B = B + ~B & (2 ** (b - a + 1) - 1 << (N - b))
print(' '.join(list(bin(B + 2 ** (N + 1))[-N:])))