triangles = [0] * 100
triangles[0], triangles[1], triangles[2], triangles[3], triangles[4] = 1, 1, 1, 2, 2
for i in range(5, 100):
    triangles[i] = triangles[i-1] + triangles[i-5]

for _ in range(int(input())):
    print(triangles[int(input())-1])
