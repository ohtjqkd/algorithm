import copy
import sys
input = sys.stdin.readline


# w() 함수를 메모이제이션해서 구하는 것이 포인트
# 하지만 키값이 많아진다면?? ㅠㅠ

# 소스는 퍼옴


dp = {}


def w(a, b, c):
    global dp
    if (a, b, c) in dp.keys():
        return dp[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        dp[(20, 20, 20)] = w(20, 20, 20)
        return dp[(20, 20, 20)]

    elif a < b < c:
        dp[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[(a, b, c)]

    else:
        dp[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + \
            w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[(a, b, c)]


while True:
    string = input().strip()
    if string == "-1 -1 -1" or not string:
        break
    a, b, c = map(int, string.split(" "))

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
