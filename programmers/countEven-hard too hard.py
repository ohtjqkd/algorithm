from itertools import combinations, permutations

a = [[1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1]]

# [0 1 0]
# [1 1 1]
# [1 1 0]
# [0 1 1]
# rules of pascal, recurrence relation c(n, r) = c(n-1, r-1) + c(n-1, r)


def pb(arr):
    for a in arr:
        print(a)


def rotate(a):
    new_a = [[0 for _ in range(len(a))] for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            new_a[j][i] = a[i][j]
    return new_a


def solution(a):
    pb(a)
    rowCombCnt = [[1 if i == 0 else 0 for i in range(
        len(a)+1)] for _ in range(len(a)+1)]
    f = [0 for _ in range(len(a[0]))]
    for n in range(1, len(a)+1):
        for r in range(1, len(a)+1):
            rowCombCnt[n][r] = rowCombCnt[n-1][r-1] + rowCombCnt[n-1][r]
    pb(rowCombCnt)
    oneCnt = [sum(i) for i in rotate(a)]
    print(oneCnt)
    f[0] = rowCombCnt[len(a)][len(a)-oneCnt[0]]
    print(f)


# all elements of b are 0 or 1
# the number of rows/columns of a is equal to rows/columns of b
# i = 1, 2, 3..(the number of columns of a)
print(solution(a))
