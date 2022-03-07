# 투포인터 문젠데 시붕..

# 메모리 초과
# for a in A:
#     tmp = []
#     while stack:
#         p = stack.pop()
#         prev_len = len(p)
#         p.add(a)
#         if prev_len != len(p):
#             tmp.append(p)
#             answer += 1
#     tmp.append(set([a]))
#     answer += 1
#     stack = tmp
# start, end = 0, 0

from collections import deque
N = int(input())
A = list(map(int, input().split(" ")))
check = [0 for _ in range(100001)]
answer = 0
q = deque([])
end = 0
while end < len(A):
    if check[A[end]] == 1 and q:
        check[q.popleft()] = 0
        continue
    q.append(A[end])
    check[A[end]] = 1
    end += 1
    answer += len(q)

print(answer)