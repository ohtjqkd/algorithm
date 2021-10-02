from collections import deque

n, m, timetable = 4, 5, [[1140,1200],[1150,1200],[1100,1200],[1210,1300],[1220,1280]]

def solution(n, m, timetable):
    maxCus = 0
    timetable.sort(key=lambda x: (-x[1], -x[0]))
    que = deque([])
    que.append(timetable.pop())
    while que or timetable:
        if not que:
            que.append(timetable.pop())
        elif timetable and que[0][1] > timetable[-1][0]:
            que.append(timetable.pop())
        else:
            que.popleft()
        print(que)
        maxCus = max(maxCus, len(que))
    print(maxCus)

solution(n, m, timetable)