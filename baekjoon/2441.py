# input: 5
# output
# *****
#  ****
#   ***
#    **
#     *

N = int(input())
for i in range(N):
    print(" "*i+"*"*(N-i))