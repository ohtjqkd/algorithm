n = int(input())

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        b, a = a%b, b
    return a
        

for _ in range(n):
    ret = 0
    arr = list(map(int, input().split(" ")))[1:]
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            ret += gcd(arr[i], arr[j])
    print(ret)