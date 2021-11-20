# input
# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13
# output
# 7
# 8
# 10
# 13
# 19
# 20
# 23

small = []
for _ in range(9):
    small.append(int(input()))

S = sum(small)

for i in range(len(small)-1):
    for j in range(i+1, len(small)):
        if small[i]+small[j] == S-100:
            del(small[j])
            del(small[i])
            break
small.sort()
for s in small:
    print(s)
