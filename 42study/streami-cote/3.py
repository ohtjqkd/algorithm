# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    check = [0 for _ in range(100001)]
    cand = set()
    for i in range(len(A)):
        if A[i] == B[i]:
            check[A[i]] = 1
    for i in range(1, 100002):
        if check[i] != 1:
            return i