

n = int(input())
strings = [input() for _ in range(n)]
ret = ""
for i in range(len(strings[0])):
    for j in range(len(strings)-1):
        if strings[j][i] != strings[j+1][i]:
            ret += "?"
            break
    else:
        ret += strings[0][i]
print(ret)
# input
# 3
# config.sys
# config.inf
# configures