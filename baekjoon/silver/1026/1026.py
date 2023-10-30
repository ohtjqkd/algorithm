# input
# 5
# 1 1 1 6 0
# 2 7 8 3 1
# output
# 18
def solution(a, b):
    ret = 0
    a.sort()
    b.sort(reverse=True)
    for i in range(len(a)):
        ret += a[i]*b[i]
    return ret

n = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
print(solution(a, b))
