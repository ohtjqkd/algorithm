import math

n = int(input())
arr = []
result = []
answer = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
m = arr[-1]-arr[0]
msqrt = math.sqrt(m)
for i in range(2, int(msqrt)+1):
    if m % i == 0:
        result.append(i)
        result.append(m//i)
result.append(m)
for i in result:
    tmp = arr[0]%i
    boolean = True
    for a in arr:
        if a % i == tmp:
            continue
        else:
            boolean = False
            break
    if boolean:
        if i not in answer:
            answer.append(i)
answer.sort()
for a in answer:
    print(a,end=' ')
