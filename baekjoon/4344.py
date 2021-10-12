c = int(input())
for _ in range(c):
    case = list(map(int, input().split()))
    n = case[0]
    sums, count = 0, 0
    for i in range(1, n+1):
        sums += case[i]
    ave = sums/n
    for i in range(1, n+1):
        if case[i] > ave:
            count += 1
    print('%.3f' % round(count/n*100, 3)+"%")
