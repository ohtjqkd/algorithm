import math
# n = 15
n = 2147483647
# n = 41
# n = 24


def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


def recur(n, threeCnt, oneCnt, totalOne):
    answer = 0
    # print(n, threeCnt, oneCnt, totalOne)
    if threeCnt < 0 or oneCnt < 0 or (threeCnt == 0 and oneCnt > 0):
        return 0
    if threeCnt == 0 and oneCnt == 0 and n == 1:
        return 1

    for i in range(oneCnt+1):
        if (n-i) % 3 == 0 and totalOne+i-2 >= 0:
            # print(n-i, totalOne+i-2)
            answer += recur((n-i)//3, threeCnt-1, oneCnt -
                            i, totalOne+i-2)
    # if not oneCnt and threeCnt % 3 == 0:
    #     answer += recur(n//3, threeCnt-1, oneCnt, totalOne-2)

    return answer


def solution(n):
    answer = 0
    threeCnt = math.floor(math.log(n, 3))
    oneCnt = threeCnt * 2
    totalThree = threeCnt
    totalOne = oneCnt
    print(math.floor(math.log(n, 3)))
    print(recur(n-2, threeCnt, oneCnt-2, 2))


solution(n)
