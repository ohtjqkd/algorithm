def solution(H: list):
    def bin_search(li, value):
        start, end = 0, len(li)
        while start < end:
            mid = (start + end) // 2
            if li[mid][0] == value:
                return mid
            elif li[mid][0] < value:
                start = mid + 1
            else:
                end = mid - 1
        return start
        
    answer = []
    for h in set(H):
        answer.append([h, 0])
    answer.sort()
    stack = []
    for i, h in enumerate(H):
        if len(stack) == 0:
            stack.append((h, i))
        else:
            while stack and stack[-1][0] > h:
                hh, ii = stack.pop()
                idx = bin_search(answer, hh)
                answer[idx][1] += (i - ii)
                if stack and stack[-1][0] != hh:
                    answer[idx][1] += 1
                elif not stack:
                    answer[idx][1] += ii
            stack.append((h, i))
    while stack:
        hh, ii = stack.pop()
        idx = bin_search(answer, hh)
        answer[idx][1] += (len(H) - ii - 1)
        if stack and stack[-1][0] != hh:
            answer[idx][1] += 1
        elif not stack:
            answer[idx][1] += ii
    print(answer)
    print(stack)
    return answer

solution([3,2,1,1,3])