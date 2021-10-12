for _ in range(int(input())):
    n, string = input().split()
    n = int(n)
    result = ''
    for c in string:
        for _ in range(n):
            result += c
    print(result)
