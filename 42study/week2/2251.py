from collections import deque
max_v = list(map(int, input().split(" ")))

mem = set()
q = deque([(0, 0, max_v[2])])
while q:
    curr = q.popleft()
    curr_mem = len(mem)
    mem.add((curr[0], curr[1], curr[2]))
    if curr_mem == len(mem):
        continue
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            tmp = [0, 0, 0]
            tmp[i] = curr[i] - min(curr[i], max_v[j] - curr[j])
            tmp[j] = curr[j] + min(curr[i], max_v[j] - curr[j])
            tmp[3 - i - j] = curr[3 - i - j]
            q.append(tuple(tmp))
result = [m[2] for m in mem if m[0] == 0]
result.sort()
print(' '.join(map(str, result)))