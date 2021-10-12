apt = [[0]*(15) for _ in range(15)]
apt[0] = [i for i in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        apt[i][j] = apt[i-1][j]+apt[i][j-1]
for _ in range(int(input())):
    k, n = int(input()), int(input())
    print(apt[k][n])
