n, m = map(int, input().split())


def pick(n, m, arr):
    if m == 0:
        for i in range(len(arr)):
            if i == len(arr)-1:
                print(arr[i])
            else:
                print(arr[i], end=' ')
    else:
        for i in range(1, n+1):
            pick(n, m-1, arr+[i])


for i in range(1, n+1):
    pick(n, m-1, [i])
