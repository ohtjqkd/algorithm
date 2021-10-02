string1 = list(input())
string2 = list(input())
len1, len2 = len(string1), len(string2)
dp = [[0] * (len1+1) for _ in range(len2+1)]

for i in range(len2):
    for j in range(len1):
        if string2[i] == string1[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(dp[len2][len1])
