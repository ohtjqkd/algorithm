n = int(input())

sum = 0


def hanoi(n, a, b, c):
    global sum
    if n == 1:
        print(a, c)
        sum += 1
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        sum += 1
        hanoi(n-1, b, a, c)


# for i in range(n-1):
#     sum = sum * 2 + 1
hanoi(n, 1, 2, 3)
print(sum)
