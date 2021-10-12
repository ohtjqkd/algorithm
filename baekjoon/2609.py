def gcd(a,b):
    if a%b == 0:
        return b
    a,b = b, a%b
    return gcd(a,b)


n, m = map(int,input().split())
k = gcd(n,m)
print(k)
print(n*m//k)
