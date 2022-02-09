from collections import defaultdict

# 투포인터 알고리즘 사용 #출처: dev-note-97.tistory.com/70

def solution(gems):
    answer = []
    min_value = len(gems) + 1 # 가장 긴 구간의 길이
    
    start, end = 0, 0

    gem_kind = len(set(gems))
    now_gem = defaultdict(int)
    now_kind = set()

    while end < len(gems):
        now_gem[gems[end]] += 1
        now_kind.add(gems[end])
        end += 1
        if len(now_kind) == gem_kind:
            while start < end:
                if now_gem[gems[start]] > 1:
                    now_gem[gems[start]] -= 1
                    start += 1
                elif min_value > end - start:
                    min_value = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break

    return answer

test_case = [
    [
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
        [3, 7]
    ],
    [
        ["AA", "AB", "AC", "AA", "AC"],
        [1, 3]
    ],
    [
        ["XYZ", "XYZ", "XYZ"],
        [1, 1]
    ],
    [
        ["ZZZ", "YYY", "NNNN", "YYY", "BBB"],
        [1, 5]
    ]
]

print(solution(test_case[3][0]))