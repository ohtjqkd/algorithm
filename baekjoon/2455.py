# input
# 0 32
# 3 13
# 28 25
# 39 0
# output: 42

max_p = 0
p = 0
for _ in range(4):
    d, u = map(int, input().split(" "))
    p = p-d
    max_p = max(max_p, p)
    p = p+u
    max_p = max(max_p, p)
print(max_p)