# input: 200
# output: 19

S = int(input())
n = 0
while (n**2+n) // 2 <= S:
    n += 1
print(n-1)