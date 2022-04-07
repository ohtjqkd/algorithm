# 부품 대여장

from collections import defaultdict
import sys

input = sys.stdin.readline
N, L, F = list(input().split(" "))
N, F = int(N), int(F)
MONTH_DAY = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
rent_info = defaultdict(dict)
fee = defaultdict(int)

for i in range(1,len(MONTH_DAY)):
    MONTH_DAY[i] += MONTH_DAY[i - 1]

def day_to_int(day, time):
    _, M, D = map(int, day.split("-"))
    h, m = map(int, time.split(":"))
    return sum([MONTH_DAY[M-1] * 24 * 60, D * 24 * 60, h * 60, m])

rd, rt = L.split("/")
rent_period = day_to_int("01-01-"+rd, rt)

for i in range(N):
    day, time, book, user = input().rstrip().split(" ")
    rent_day = rent_info.get(user, dict()).get(book, 0)
    if rent_day == 0:
        rent_info[user][book] = day_to_int(day, time)
    else:
        now = day_to_int(day, time)
        if now - rent_day > rent_period:
            fee[user] += (now - rent_day - rent_period) * F
        rent_info[user][book] = 0
result = sorted(fee.items())

if result:
    for r in result:
        print(r[0], r[1])
else:
    print(-1)
