from distutils.file_util import write_file
from heapq import heappush, heappop
from collections import deque
import sys

sys.setrecursionlimit = 100000000
def solution(alp, cop, problems):
    req_a, req_c = max(problems, key = lambda x: x[0])[0], max(problems, key = lambda x: x[1])[1]
    dp = [[float('inf') for _ in range(req_a + 1)] for _ in range(req_c + 1)]
    for i in range(alp + 1):
        for j in range(cop + 1):
            dp[j][i] = 0
    for i in range(req_c + 1):
        for j in range(req_a + 1):
            if i + 1 < req_c + 1:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            if j + 1 < req_a + 1:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
            for ar, cr, ad, cd, co in problems:
                if j + ad < req_a + 1 and i + cd < req_c + 1 and ar <= j and cr <= i:
                    dp[i + cd][j + ad] = min(dp[i][j] + co, dp[i + cd][j + ad])
    return dp[req_c][req_a]
tc = [[10,	10,	[[10,15,2,1,2],[20,20,3,3,4]],	15],
[0,	0,	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]],	13]]

for t in tc:
    print(solution(t[0], t[1], t[2]))