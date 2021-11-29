# input
# 14 30 0
# 200
# output: 14 33 20

A, B, C = map(int, input().split(" "))
D = int(input())
total = A*60*60 + B*60 + C + D
total, C = total//60, total % 60
total, B = total//60, total % 60
A = total % 24
print(A, B, C)