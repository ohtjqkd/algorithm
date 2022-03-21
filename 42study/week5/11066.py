# 파일 합치기

# dp 그려서 생각해보기! -> 어렵다 - - 어지러워 
import sys

input = sys.stdin.readline

# 시간초과 solution T _ T but pypy3에서는 느리지만 통과
def solution():
    N = int(input())
    pages = list(map(int, input().split(" ")))
    S = [[pages[i] if i == j else 0 for i in range(N)] for j in range(N)]
    dp = [[pages[i] if i == j else float('inf') for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            if j - i == 1:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j]
            S[i][j] = S[i][j - 1] + S[j][j]

    for i in range(2, N):
        for j in range(N - i):
            for k in range(i):
                r = dp[j][j + k] if j != j + k else 0
                c = dp[j + k + 1][i + j] if j + k + 1!= i + j else 0
                dp[j][i + j] = min(dp[j][i + j], r + c + S[j][i + j])

    print(dp[0][N - 1])

T = int(input())

for _ in range(T):
    solution()
#   1   22  49
#       21  24  35
#           3   7
#               4


# 1   22  25  29  34  69  74  78  81

#     21  24  28  33  68  73  77  80

#         3   7   12  47  52  56  59

#             4   9   44  49  53  56

#                 5   40  45  49  52

#                     35  40  44  47

#                         5   9   12

#                             4   7

#                                 3   

#                                     5

#                                         98

#                                             21

#                                                 14

#                                                     17

#                                                         32

# 40  70  160 300  190+350

#     30  60  170  300

#         30  80   200

#             50   90

#                  40