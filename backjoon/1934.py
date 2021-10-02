def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b != 0:
        return gcd(a % b, b)
    else:
        return b


for i in range(int(input())):
    a, b = map(int, input().split(" "))
    print(a*b//gcd(a, b))
