# input
# 9
# 1 1 230
# 1 2 210
# 1 3 205
# 2 1 100
# 2 2 150
# 3 1 175
# 3 2 190
# 3 3 180
# 3 4 195
# output
# 1 1
# 1 2
# 3 4

N = int(input())
nat, print_cnt = [0 for _ in range(N+1)], 0
tables = [list(map(int, input().split(" "))) for _ in range(N)]
tables.sort(key=lambda x: x[2])
while print_cnt < 3:
    a, b, _ = tables.pop()
    if nat[a] >= 2:
        continue
    print(a, b)
    nat[a] += 1
    print_cnt += 1
