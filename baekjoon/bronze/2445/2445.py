# input: 5
# output
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

N = int(input())
for i in range(N*2-1):
    empty = abs(N-i-1)
    star = N-empty
    print("*"*star+" "*empty*2+"*"*star)