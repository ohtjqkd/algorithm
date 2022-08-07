from collections import defaultdict


N = int(input())

hold_loc = [[-1, -1] for _ in range(N ** 2)]
preference = dict()

def getNear(curr, hold_loc):
    dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
    curr_loc = preference.get(curr)
    if curr_loc:
        for i in range(4):
            xx, yy = curr[0] + dx[i], curr[1] + dy[i]

    return 
for i in range(N ** 2):
    L = list(map(int, input().split(" ")))
    preference = L[1:]
    # preference[L[0] - 1] = L[1:]
    candidate = defaultdict(int)
    for p in preference:
        loc = preference.get(p)
        dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
        curr_loc = preference.get(p)
        if curr_loc:
            for i in range(4):
                xx, yy = curr_loc[0] + dx[i], curr_loc[1] + dy[i]
                candidate[(xx, yy)] += 1