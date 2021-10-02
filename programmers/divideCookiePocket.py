from copy import deepcopy

cookie = [1, 1, 2, 3]
# cookie = [1, 2, 4, 5]


def solution(cookie):
    answer = 0
    for i in range(1, len(cookie)):
        new_cookie = deepcopy(cookie)
        first, second = new_cookie[:i], list(reversed(new_cookie[i:]))
        first_sum, second_sum = 0, 0
        print(first, second)
        while first or second:
            if (not first and second_sum > first_sum) or (not second and first_sum > second_sum):
                break
            if first_sum >= second_sum and second:
                second_sum += second.pop()
            elif first_sum < second_sum and first:
                first_sum += first.pop()
            if first_sum == second_sum:
                answer = max(answer, first_sum)
                if first:
                    first_sum += first.pop()
                if second:
                    second_sum += second.pop()
        if first_sum == second_sum:
            answer = max(answer, first_sum)
    return answer


print(solution(cookie))
