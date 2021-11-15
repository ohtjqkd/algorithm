# input
# 2
# ABC-0123
# AAA-9999

N = int(input())
alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
dic = dict(zip(alph, range(len(alph))))
for _ in range(N):
    p, n = input().split("-")
    S = sum([26**(2-i)*dic[p[i]] for i in range(len(p))])
    if abs(S-int(n)) <= 100:
        print("nice")
    else:
        print("not nice")