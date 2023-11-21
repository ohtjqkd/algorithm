n, m = map(int, input().split())


def pick(n, m, arr):
    if m == 0:
        for i in arr:
            print(i, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if i not in arr:
                pick(n, m-1, arr+[i])


pick(n, m, [])
