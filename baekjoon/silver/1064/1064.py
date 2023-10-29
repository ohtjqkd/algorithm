# input
# 1 2 3 4 8 7
# output
# 11.547796284592874

import math
x1, y1, x2, y2, x3, y3 = map(int, input().split())
rn = float('inf')
rx = 0
dots = [(x1, y1), (x2, y2), (x3, y3)]
for i in range(len(dots)):
  vx1, vy1 = dots[i]
  vx2, vy2 = dots[(i + 1) % 3]
  vx3, vy3 = dots[(i + 2) % 3]
  xx1, yy1 = vx2 - vx1, vy2 - vy1
  xx2, yy2 = vx3 - vx1, vy3 - vy1
  if xx1 == 0 and xx2 == 0:
    continue
  elif xx1 != 0 and xx2 != 0 and yy1 / xx1 == yy2 / xx2:
    continue
  else:
    rn = min(rn, math.sqrt(xx1 ** 2 + yy1 ** 2) + math.sqrt(xx2 ** 2 + yy2 ** 2))
    rx = max(rx, math.sqrt(xx1 ** 2 + yy1 ** 2) + math.sqrt(xx2 ** 2 + yy2 ** 2))
if rx == 0:
  print('-1.0')
else:
  print(rx * 2 - rn * 2)
