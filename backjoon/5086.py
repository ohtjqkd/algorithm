

while True:
    n, m = map(int,(input().split()))
    result = 0
    if n == 0 and m == 0:
        break
    if n == 0 or m == 0:
        print('neither')
        continue
    if m%n == 0:
        result+=1
    if n%m == 0:
        result+=2
    if result == 0:
        print('neither')
    elif result == 1:
        print('factor')
    else:
        print('multiple')

