from itertools import combinations
from collections import defaultdict

# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
Order = ["XYZ", "XWY", "WXA"]
Course = [2, 3, 4]


def solution(orders, course):
    answer = []
    for c in course:
        dic = defaultdict(int)
        maxs = 0
        for order in orders:
            order = list(order)
            order.sort()
            combs = list(combinations(order, c))
            for comb in combs:
                dic[comb] += 1
                maxs = max(maxs, dic[comb])
        for item in dic.items():
            if item[1] == maxs and item[1] >= 2:
                answer.append("".join(item[0]))
    answer.sort()
    return answer


print(solution(Order, Course))
