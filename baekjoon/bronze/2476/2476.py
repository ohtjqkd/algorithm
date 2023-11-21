# input
# 3
# 3 3 6
# 2 2 2
# 6 2 5
# output: 12000

N = int(input())
dots = [list(map(int, input().split(" "))) for _ in range(N)]
ret = []
for dot in dots:
    dot.sort()
    if dot[0] != dot[1] and dot[1] != dot[2]:
        ret.append(dot[2]*100)
    elif dot[0] == dot[1] and dot[1] == dot[2]:
        ret.append(10000+dot[0]*1000)
    else:
        ret.append(1000+dot[1]*100)

print(max(ret))
