# input
# 12345123
# 17772345
# 22233331
# output
# 1
# 3
# 4

tc = [input() for _ in range(3)]


for t in tc:
    max_l = 1
    dp = [1 for _ in range(len(t))]
    for i in range(1, len(t)):
        if t[i] == t[i-1]:
            dp[i] += dp[i-1]
    print(max(dp))