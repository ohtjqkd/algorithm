import sys
sys.setrecursionlimit(10000)

def factorial(a):
    if a == 0:
        return 1
    if a < 2:
        return a
    return a*factorial(a-1)

n, k = map(int, input().split())

print(factorial(n)//(factorial(k)*(factorial(n-k)))%10007)