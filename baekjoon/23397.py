import sys

input = sys.stdin.readline

T, D, M = map(int, input().rstrip().split(" "))
start = 0
for _ in range(M):
    meal_t = int(input().rstrip())
    if meal_t - start > T - 1:
        print("Y")
        break
    start = meal_t
else:
    if D - start > T - 1:
        print("Y")
    else:
        print("N")