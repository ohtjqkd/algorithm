def solution(n, left, right):
    answer = [0 for _ in range(right-left+1)]
    for i in range(right-left+1):
        d, m = divmod(left+i, n)
        if d > m:
            answer[i] = d+1
        else:
            answer[i] = m+1
    return answer

n, left, right = 4, 7, 14
print(solution(n, left, right))