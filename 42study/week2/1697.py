from collections import deque
n, k = map(int, input().split(' '))

## answer code
# MAX = 100001
# array = [0] * MAX

# def bfs():
#     q = deque([n])
#     while q:
#         now_pos = q.popleft()
#         if now_pos == k:
#             return array[now_pos]
#         for next_pos in (now_pos-1, now_pos+1, now_pos*2):
#             if 0 <= next_pos < MAX and not array[next_pos]:
#                 array[next_pos] = array[now_pos] + 1
#                 q.append(next_pos)

# print(bfs())

def bfs():
    q = deque([set([n])])
    t = [float('inf') for _ in range(100001)]
    dept = 0
    while q:
        currs = q.popleft()
        nxt_dept = set()
        for curr in currs:
            if curr == k:
                return dept
            if curr < 0 or curr > 100000 or t[curr] <= dept:
                continue
            t[curr] = dept + 1
            nxt_dept.add(curr+1)
            nxt_dept.add(curr-1)
            nxt_dept.add(curr*2)
        if len(nxt_dept) != 0:
            q.append(nxt_dept)
        dept += 1
print(bfs())