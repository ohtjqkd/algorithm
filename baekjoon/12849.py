D = int(input())


# 0: 정보과학관
# 1: 전산관
# 2: 미래관
# 3: 신앙관
# 4: 한경직기념관
# 5: 진리관
# 6: 학생회관
# 7: 형남공학관
nodes = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3, 4],
    3: [1, 2, 4, 5],
    4: [2, 3, 5, 6],
    5: [3, 4, 7],
    6: [4, 7],
    7: [5, 6]
}

dp = [0 for _ in range(8)]
dp[0] = 1

for _ in range(D):
    new_dp = [0 for _ in range(8)]
    for i in range(8):
        if dp[i] != 0:
            next_nodes = nodes[i]
            for next in next_nodes:
                new_dp[next] += dp[i]
    dp = [i % 1000000007 for i in new_dp]

print(dp[0])


# 풀이

dp = [1, 0, 0, 0, 0, 0, 0, 0]


def nxt(state):
    tmp = [0 for _ in range(8)]
    tmp[0] = state[1] + state[2]
    tmp[1] = state[0] + state[2] + state[3]
    tmp[2] = state[0] + state[1] + state[3] + state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[6]
    tmp[5] = state[3] + state[4] + state[7]
    tmp[6] = state[4] + state[7]
    tmp[7] = state[5] + state[6]
    tmp = [i % 1000000007 for i in tmp]
    return tmp


for _ in range(D):
    dp = nxt(dp)
print(dp[0])
