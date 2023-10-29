# input
# 5
# 5 4 1 3 2
# output
# Nice

n = int(input())

front = list(map(int, input().split(' ')))

front.reverse()

s = []

n = 1

while front or s:
  if len(s) != 0 and s[-1] == n:
    s.pop()
    n += 1
  else:
    if front:
      p = front.pop()
      if p != n:
        s.append(p)
      else:
        n += 1
    else:
      break
if s:
  print('Sad')
else:
  print('Nice')
  
  