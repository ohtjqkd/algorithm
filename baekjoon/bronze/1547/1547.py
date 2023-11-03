# input
# 4
# 3 1
# 2 3
# 3 1
# 3 2

# output
# 3

now_loc = 1
move_cnt = int(input())
for _ in range(move_cnt):
    n1, n2 = tuple(map(int, input().split(" ")))
    if n1 == now_loc:
        now_loc = n2
    elif n2 == now_loc:
        now_loc = n1

print(now_loc)