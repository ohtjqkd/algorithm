from collections import deque
N, K = map(int, input().split(" "))
D = list(map(int, input().split(" ")))
answer = float('inf')
idx, doll_cnt = 0, [0, 0]
q = deque([])
while idx < len(D):
    doll_cnt[D[idx] - 1] += 1
    q.append(D[idx])
    idx += 1
    while doll_cnt[0] >= K and q:
        answer = min(answer, len(q))
        doll_cnt[q.popleft() - 1] -= 1
if answer == float('inf'):
    print(-1)
else:
    print(answer)