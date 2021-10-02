n = int(input())
steps = [0]*300
for i in range(n):
    steps[i] = int(input())


# m[n][0] n-1 스탭에서 오는 경우의 최대값, m[n][1] n-2 스탭에서 오는 경우의 최대값
max_v = [[0, 0] for _ in range(300)]
max_v[0][0], max_v[1][0], max_v[2][0] = \
    steps[0], steps[1] + steps[0], steps[1]+steps[2]
max_v[0][1], max_v[1][1], max_v[2][1] = \
    steps[0], steps[1], steps[0]+steps[2]

for i in range(3, n):
    max_v[i][0] = steps[i] + max_v[i-1][1]
    max_v[i][1] = steps[i] + max(max_v[i-2])

print(max(max_v[n-1]))
