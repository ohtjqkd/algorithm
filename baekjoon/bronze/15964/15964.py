# input: 4 3, 3 4
# output: 7, -7

def atOper(A, B):
    return (A+B)*(A-B)

A, B = map(int, input().split(" "))
print(atOper(A, B))
