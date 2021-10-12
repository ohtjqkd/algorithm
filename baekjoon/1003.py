for _ in range(int(input())):
    n = int(input())
    z1, o1, z2, o2 = 1, 0, 0, 1
    for _ in range(n-1):
        z1, o1, z2, o2 = z2, o2, z1+z2, o1+o2
    if n == 0:
        print(z1, o1)
    else:
        print(z2, o2)
