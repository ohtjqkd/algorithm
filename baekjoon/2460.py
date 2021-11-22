# input
# 0 32
# 3 13
# 28 25
# 17 5
# 21 20
# 11 0
# 12 12
# 4 2
# 0 8
# 21 0
# output: 42

p = 0
max_p = 0
for _ in range(10):
    d, u = map(int, input().split(" "))
    p -= d
    max_p = max(max_p, p)
    p += u
    max_p = max(max_p, p)
print(max_p)

