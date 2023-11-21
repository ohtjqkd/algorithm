import sys

inputs = sys.stdin.readline

n, k, x, y = map(int, input().rstrip().split(" "))

result = 0
for i in range(n):
    xi, yi = map(int, input().rstrip().split(" "))
    if (x - xi) ** 2 + (y - yi) ** 2 > k ** 2:
        result += 1
print(result)

# value error 왜?? 개행문자가 같이 들어온다 - - 빡치네 그래서 map에서 에러가 남
# n, k, x, y = map(int, input().split(" "))

# result = 0
# for _ in range(n):
#     xi, yi = map(int, input().split(" "))
#     if (x - xi) * (x - xi) + (y - yi) * (y - yi) > k * k:
#         result += 1
# print(result)