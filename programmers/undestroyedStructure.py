

def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    dp = [[0 for _ in range(M + 2)] for _ in range(N + 2)] # padding + 2
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            sign = -1
        else:
            sign = 1
        dp[r1 + 1][c1 + 1] += (sign * d)
        dp[r2 + 2][c2 + 2] += (sign * d) # key point!
        dp[r1 + 1][c2 + 2] -= (sign * d)
        dp[r2 + 2][c1 + 1] -= (sign * d)
    for n in range(1, N + 2):
        for m in range(1, M + 2):
            dp[n][m] += dp[n][m-1]
    for m in range(1, M + 2):
        for n in range(1, N + 2):
            dp[n][m] += dp[n-1][m]

    for i in range(N):
        for j in range(M):
            if board[i][j] + dp[i+1][j+1] > 0:
                answer += 1
    return answer

test = [
    [
        [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
    	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]],
        10
    ],
    [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]],
        6
    ]
]

print(solution(test[1][0], test[1][1]))