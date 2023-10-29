# imput
# 2
# -5 1 12 1
# 7
# 1 1 8
# -3 -1 1
# 2 2 2
# 5 5 1
# -4 5 1
# 12 1 1
# 12 1 2
# -5 1 5 1
# 1
# 0 0 2

# output
# 3
# 0
T = int(input())

for _ in range(T):
  arrival_dest = list(map(int, input().split(' ')))
  n = int(input())
  include_circle = [False] * n
  circle_info = []
  for i in range(n):
    circle_info.append(list(map(int, input().split(' '))))

  for idx, circle in enumerate(circle_info):
    if (arrival_dest[0] - circle[0]) ** 2 + (arrival_dest[1] - circle[1]) ** 2 < circle[2] ** 2:
      include_circle[idx] = not include_circle[idx]
    if (arrival_dest[2] - circle[0]) ** 2 + (arrival_dest[3] - circle[1]) ** 2 < circle[2] ** 2:
      include_circle[idx] = not include_circle[idx]
  print(include_circle.count(True))
  