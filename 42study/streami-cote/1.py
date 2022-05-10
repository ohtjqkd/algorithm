# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    if A + B < 4:
        return 0
    start, end = 0, max(A, B) + 1
    def is_possible(side_len):
        if A // side_len + B // side_len >= 4:
            return True
        return False
    while start <= end:
        mid = (start + end) // 2
        if is_possible(mid):
            start = mid + 1
        else:
            end = mid - 1
    mid = (start + end) // 2
    return mid
