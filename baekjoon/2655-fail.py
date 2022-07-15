# 가장 긴 증가하는 부분 수열(LIS)의 심화 변형 문제라고 함

from copy import deepcopy


n = int(input())
bricks = [list(map(int, input().split(" "))) + [i + 1] for i in range(n)]
bricks.append([0, 0, 0, 0])
bricks.sort(key=lambda x: (x[2], x[0]))

dp = [[0, []] for _ in range(len(bricks))]

for i in range(1, len(bricks)):
    for j in range(i):
        if bricks[i][0] > bricks[j][0]:
            if dp[i][0] < dp[j][0] + bricks[i][1]:
                dp[i] = deepcopy(dp[j])
                dp[i][0] += bricks[i][1]
                dp[i][1].append(i)
            # dp[i] = max(dp[i], dp[j] + bricks[i][1])
        # print(dp)
max_height = max(dp)
print(len(max_height[1]))
for n in reversed(max_height[1]):
    print(n)
# from collections import defaultdict

# upper_brick = defaultdict(list)
# mem = defaultdict(list)
# n = int(input())
# bricks = [list(map(int, input().split(" "))) + [i + 1] for i in range(n)]
# used = [0 for _ in range(len(bricks))]
# for i in range(len(bricks)):
#     for j in range(len(bricks)):
#         if i == j: continue
#         if bricks[i][0] > bricks[j][0] and bricks[i][2] > bricks[j][2]:
#             upper_brick[i].append(j)
# def back_tracking(idx: list):
#     print(mem)
#     if not mem.get(idx):
#         ret = [0, []]
#         brick_height = bricks[idx][1]
#         if not upper_brick.get(idx):
#             return [brick_height, [idx]]
#         for i in upper_brick.get(idx, []):
#             used[i] = 1
#             tmp = back_tracking(i)
#             print('tmp', tmp)
#             if ret[0] < tmp[0]:
#                 ret = tmp
#             used[i] = 0
#         ret[0] += brick_height
#         ret[1].append(idx)
#         return ret
#     else:
#         return mem.get(idx)
# ret = [0, []]
# for i in range(len(bricks)):
#     result = back_tracking(i)
#     if ret[0] < result[0]:
#         ret = result
# print(len(ret[1]))
# for r in ret[1]:
#     print(r[3])