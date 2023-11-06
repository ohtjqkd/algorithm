#input: 5
# output
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
N = int(input())
for i in range(N*2-1):
    empty = abs(N-1-i)
    print(" "*empty+"*"*((N-empty)*2-1))