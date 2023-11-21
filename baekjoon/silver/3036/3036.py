def gcd(a,b):
    if a<b:
        a,b = b,a
    if a == 0:
        return b
    if a%b==0:
        return b
    return gcd(b,a%b)

n = int(input())
arr=list(map(int, input().split()))
start = arr[0]

for i in range(1, len(arr)):
    gcd_v = gcd(start,arr[i])
    print(str(start//gcd_v)+'/'+str(arr[i]//gcd_v))
    
