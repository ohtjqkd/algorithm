# 1, 2, 3 더하기

# dp[n - 1]에서 앞뒤로 1을 붙여주는 경우
# dp[n - 2]에서 앞뒤로 2를 붙여주는 경우
# dp[n - 3]에서 앞뒤로 3을 붙여주는 경우
# 중복을 피하기 위해 set자료형으로 구현함 다른 풀이와 속도는 비슷한데 n이 커질 수록 시간이 많이 늘어날듯
import sys

input = sys.stdin.readline
T = int(input())
n = 11
# dp = [set() for _ in range(n)]
# dp[0].add("1")
# dp[1].add("2")
# dp[2].add("3")

# for i in range(n):
#     curr = dp[i]
#     for strs in curr:
#         if i + 1 < n:
#             dp[i + 1].add(strs + "1")
#             dp[i + 1].add("1" + strs)
#         if i + 2 < n:
#             dp[i + 2].add(strs + "2")
#             dp[i + 2].add("2" + strs)
#         if i + 3 < n:
#             dp[i + 3].add(strs + "3")
#             dp[i + 3].add("3" + strs)
# for _ in range(T):
#     print(len(dp[int(input()) - 1]))

# 다른 풀이 -> 이게 가능한 이유가 뭐지 중복처리가 되나? dp의 정의를 떠올려봅시다.!!
# !!! 뒤에 붙이는 경우만 생각하면 굳이 중복처리를 하지 않아도 되는 듯!

dp = [0] * 11
dp[:3] = [1, 1, 1]
for i in range(n):
    if i + 1 < n:
        dp[i + 1] += dp[i]
    if i + 2 < n:
        dp[i + 2] += dp[i]
    if i + 3 < n:
        dp[i + 3] += dp[i]

for _ in range(T):
    print(dp[int(input()) - 1])