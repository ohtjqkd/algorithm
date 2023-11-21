# input
# 2
# HPC PJVYMIY
# BLMRGJIASOPZEFDCKWYHUNXQTV
# FDY GAI BG UKMY
# KIMHOTSQYRLCUZPAGWJNBVDXEF
# output
# ACM CONTEST
# THE SKY IS BLUE
start = ord("A")

for _ in range(int(input())):
    crypt = list(input())
    code = input()
    for i, c in enumerate(crypt):
        if c == " ":
            continue
        crypt[i] = code[ord(c)-start]
    print(''.join(crypt))