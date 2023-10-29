# input
# 5
# 1 6
# 3 7
# 6 2
# 7 100
# 9 635
# output
# 1
# 7
# 6
# 1
# 9

T = int(input())

for i in range(T):
  a, b = map(int, input().split(' '))
  a %= 10
  if a == 0:
    print(10)
  elif a == 1 or a == 5 or a == 6:
    print(a)
  elif a == 4 or a == 9:
    b %= 2
    if b == 0:
      print((a ** 2) % 10)
    else:
      print(a)
  else:
    b %= 4
    if b == 0:
      print((a ** 4) % 10 % 10 % 10)
    else:
      print((a ** b) % 10 % 10 % 10)