# input
# 2 7
# 3 5
# output
# 31 35

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        b, a = a%b, b
    return a

o1, u1 = map(int, input().split(" "))
o2, u2 = map(int, input().split(" "))

g = gcd(u1, u2)

o = ((o1*u2)+(o2*u1))//g
u = u1*u2//g
g = gcd(o, u)
print(o//g, u//g)