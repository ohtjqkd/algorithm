# input
# 10
# 40
# 30
# 60
# 30
# output
# 34
# 30

n = [int(input()) for _ in range(5)]
n.sort()
print(sum(n)//5)
print(n[2])