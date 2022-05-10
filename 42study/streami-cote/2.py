# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.6
    ret = 0
    max_cost = C[0]
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            max_cost = max(max_cost, C[i])
            C[i] += C[i - 1]
        else:
            ret += C[i - 1] - max_cost
            max_cost = C[i]
    ret += C[-1] - max_cost
    return ret
