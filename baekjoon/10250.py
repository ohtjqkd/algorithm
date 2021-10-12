for _ in range(int(input())):
    h, w, n = map(int, input().split())
    n -= 1
    c, r = n//h+1, n % h + 1
    print(str(r)+'%02d' % c)
