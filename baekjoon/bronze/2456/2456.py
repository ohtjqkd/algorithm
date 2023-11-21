# input
# 6
# 3 1 2
# 2 3 1
# 3 1 2
# 1 2 3
# 3 1 2
# 1 2 3
# output: 1 13

p = int(input())
cand = [[0, 0, 0, 0, i] for i in range(3)]
for _ in range(p):
    c1, c2, c3 = map(int, input().split(" "))
    cand[0][c1] += 1
    cand[0][0] += c1
    cand[1][c2] += 1
    cand[1][0] += c2
    cand[2][c3] += 1
    cand[2][0] += c3
cand.sort(reverse=True)
if cand[0][:3] == cand[1][:3]:
    print(0, cand[0][0])
else:
    print(cand[0][4]+1, cand[0][0])