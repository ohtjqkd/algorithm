# input: 5
# output
#     *
#    ***
#   *****
#  *******
# *********
N = int(input())
for i in range(N):
    print(" "*(N-i-1)+"*"*(i*2+1))