# 문자열 제거
# 몰라

import sys

input = sys.stdin.readline

S = list(input().rstrip())
M = int(input().rstrip())
A = []
result = 0
for i in range(M):
    a, n = input().split(" ")
    A.append((int(n), a))
A.sort(key=lambda x: x[0]/len(x[1]))
def find_str(s1, s2, start, idx):
    if idx == len(s2):
        return True
    tmp = s1[start + idx]
    if s1[start + idx] == s2[idx]:
        s1[start + idx] = '_'
        if not find_str(s1, s2, start, idx + 1):
            s1[start + idx] = tmp
        else:
            return True
    else:
        return False

while A:
    score, curr_str = A.pop()
    if score // len(curr_str) < 1:
        break
    for i in range(len(S) - len(curr_str) + 1):
        if i != '_':
            if find_str(S, curr_str, i, 0):
                result += score
for c in S:
    if c != '_':
        result += 1

print(result)