# input
# 3
# 1 2 3

seats = [0 for _ in range(100)]
p = int(input())
wish_seats = list(map(lambda x: int(x)-1, input().split(" ")))
ret = 0
for s in wish_seats:
    if seats[s] == 0:
        seats[s] = 1
    else:
        ret += 1
print(ret)

