# input
# 3 5
# 1 2 4
# 2 3 4 5 6

a, b = list(map(int, input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a^b))
