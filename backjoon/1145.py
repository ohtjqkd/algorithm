arr = list(map(int, input().split(" ")))

def comb(arr, n):
    ret = []
    if n > len(arr): return ret
    if n == 1:
        for i in arr:
            ret.append([i])
    elif n > 1:
        for i in range(len(arr)-n+1):
            for temp in comb(arr[i+1:], n-1):
                ret.append([arr[i]]+temp)
    return ret

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a
ret = float('inf')
for a, b, c in comb(arr, 3):
    a = a*b/gcd(a, b)
    a = a*c/gcd(a, c)
    ret = min(ret, a)

print(int(ret))
    


# input
# 30 42 70 35 90