a, b, v = map(int, input().split())
if a == v:
    print(1)
else:
    day = 0
    top = v-a
    day += 1
    day += top // (a-b)
    if top % (a-b) != 0:
        day += 1
    print(day)
