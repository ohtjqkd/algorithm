# input
# 8
# 71 39 44
# 32 83 55
# 51 37 63
# 89 29 100
# 83 58 11
# 65 13 15
# 47 25 29
# 60 66 19
# output
# 253

# import sys


# def rgb(n, m):
#     result = 0
#     if m == M-1:
#         return cost[m][n]
#     if n == 0:
#         result = cost[m][n]+min(rgb(1, m+1), rgb(2, m+1))

#     elif n == 1:
#         result = cost[m][n]+min(rgb(0, m+1), rgb(2, m+1))

#     elif n == 2:
#         result = cost[m][n]+min(rgb(0, m+1), rgb(1, m+1))
#     return result

n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

min_cost = [[0]*3 for _ in range(n)]
min_cost[0][0], min_cost[0][1], min_cost[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, n):
    for j in range(3):
        min_cost[i][j] = cost[i][j] + \
            min(min_cost[i-1][j-1], min_cost[i-1][j-2])

print(min(min_cost[n-1]))
# print(min(rgb(0, 0), rgb(1, 0), rgb(2, 0)))
