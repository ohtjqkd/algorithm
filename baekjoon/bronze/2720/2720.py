# input
# 3
# 124
# 25
# 194
# output
# 4 2 0 4
# 1 0 0 0
# 7 1 1 4
coins = [25, 10, 5, 1]
for _ in range(int(input())):
    t = int(input())
    for i in range(4):
        print(t // coins[i], end=" ")
        t %= coins[i]
    print()