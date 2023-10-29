# input
# 2008 12 27
# 2009 1 22
# output
# D-26

import datetime

leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
norm_year = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(1, 12):
  leap_year[i] = leap_year[i] + leap_year[i-1]
  norm_year[i] = norm_year[i] + norm_year[i-1]

s_y, s_m, s_d = map(int, input().split())
e_y, e_m, e_d = map(int, input().split())

s_dt = datetime.datetime(s_y, s_m, s_d)
e_dt = datetime.datetime(e_y, e_m, e_d)

ans = 0

def is_leap_year(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False

if datetime.datetime(s_y + 1000, s_m, s_d) <= e_dt:
  print('gg')
else:
  for i in range(s_y, e_y):
    if is_leap_year(i):
      ans += 366
    else:
      ans += 365
  if s_m != 1:
    if is_leap_year(s_y):
      ans -= leap_year[s_m - 2]
    else:
      ans -= norm_year[s_m - 2]
  if e_m != 1:
    if is_leap_year(e_y) and e_m:
      ans += leap_year[e_m - 2]
    else:
      ans += norm_year[e_m - 2]
  ans -= s_d
  ans += e_d
  print(f'D-{ans}')