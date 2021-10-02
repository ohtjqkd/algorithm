from collections import deque

N, K = map(int, input().split(" "))
ret = []
deq = deque([i for i in range(1, N+1)])
cnt = 0
while len(deq):
    cnt += 1
    if cnt == K:
        ret.append(deq.popleft())
        cnt = 0
    else:
        deq.append(deq.popleft())

answer = ", ".join(map(str, ret))

print(f"<{answer}>")
