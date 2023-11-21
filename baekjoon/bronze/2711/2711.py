# input
# 4
# 4 MISSPELL
# 1 PROGRAMMING
# 7 CONTEST
# 3 BALLOON
# output
# MISPELL
# ROGRAMMING
# CONTES
# BALOON

for _ in range(int(input())):
    t, s = input().split(" ")
    s = list(s)
    del(s[int(t)-1])
    print(''.join(s))