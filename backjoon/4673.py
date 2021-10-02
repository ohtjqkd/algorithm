def selfn(a):
    answer = a
    arr = list(map(int, list(str(a))))
    answer += sum(arr)
    return answer


visited = [0]*10000
for i in range(1, 10000):
    s = selfn(i)
    if s < 10000:
        visited[selfn(i)] = 1
for idx, v in enumerate(visited):
    if idx == 0:
        continue
    if not v:
        print(idx)
