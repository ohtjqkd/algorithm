n = int(input())
p = []
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x, y))
for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            rank += 1
    print(rank, end=' ')
