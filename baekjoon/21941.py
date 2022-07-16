# input
# abcxyzxabc
# 2
# abc 10
# xyz 5


import heapq as hq

S = list(input())
M = int(input())
SCORE = 0
heap = []

for _ in range(M):
    s, score = input().split(" ")
    score = int(score)
    hq.heappush(heap, (-score/len(s), s, score))

def replace(src, target):
    src_len, target_len, i, result = len(src), len(target), 0, 0
    while i < src_len - target_len + 1:
        j = 0
        flag = False
        while i + j < src_len and src[i + j] == target[j]:
            if j == target_len - 1:
                flag = True
                break
            j += 1
        if flag:
            for k in range(j + 1):
                src[i + k] = '_'
            result += 1
            i += j
        else:
            i += 1
    return result

while heap:
    eff, s, score = hq.heappop(heap)
    if eff > -1:
        break
    replaced = replace(S, s)
    SCORE += replaced * score
for s in S:
    if s != '_':
        SCORE += 1
print(SCORE)