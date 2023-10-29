# input
# 199 121
# output
# 24079

def gcd(a, b):
  if(b == 0):
    return a
  return gcd(b, a%b)

def lcm(a, b):
  return a * b // gcd(a, b)

a, b = map(int, input().split(' '))

print(lcm(a, b))

