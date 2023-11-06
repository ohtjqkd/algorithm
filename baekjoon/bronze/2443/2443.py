# input: 5
# output
# *********
#  *******
#   *****
#    ***
#     *

N = int(input())
for i in range(N):
    print(" "*i+"*"*(2*(N-i)-1))