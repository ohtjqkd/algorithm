from collections import defaultdict
from itertools import permutations
tc = [[["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "abc1**"], 2], 
[["frodo", "fradi", "crodo", "abc123", "frodoc"],	["*rodo", "*rodo", "******"], 2],
[["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"],	3]]
def combination(arr, cnt):
    ret = []
    if cnt == 0:
        return [[]]
    for i in range(len(arr)):
        for C in combination(arr[i+1:], cnt - 1):
            ret.append([arr[i]] + C)
    return ret

def is_possible(wild_str, target_str):
    if len(wild_str) != len(target_str):
        return False
    for i in range(len(wild_str)):
        if wild_str[i] == "*" or wild_str[i] == target_str[i]:
            continue
        else:
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    cand = combination(user_id, len(banned_id))
    uid_possible = defaultdict(set)
    for uid in user_id:
        for bid in banned_id:
            if is_possible(bid, uid):
                uid_possible[uid].add(bid)

    perm = list(permutations(banned_id))
    for c in cand:
        for p in perm:
            for z in zip(c, p):
                if z[1] not in uid_possible[z[0]]:
                    break
            else:
                answer += 1
                break
    return answer

for i,c in enumerate(tc):
    # if i == 2:
    print(solution(c[0], c[1]) == c[2])
    print()