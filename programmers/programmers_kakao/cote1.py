arr = [[1, 2], [2, 4], [2, 2]]
arr = [[1, 4], [2, 6], [4, 7]]
def solution(arr):
    if len(arr) == 0: return 0
    answer = 1
    arr.sort(key=lambda x: (-x[1],-x[0]))
    stack = [arr.pop()]
    # print(stack)
    while stack and arr:
        nxt_start, nxt_end = arr.pop()
        # print(stack, arr)
        if stack[-1][1] <= nxt_start:
            answer += 1
            stack.pop()
            stack.append([nxt_start,nxt_end])

    # print(answer)
    return answer

solution(arr)