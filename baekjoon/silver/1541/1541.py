s = input()

e = []

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

curr = 0
ans = 0
for i in range(1, len(s)):
  if s[i] == '-' or s[i] == '+':
    e.append(int(s[curr:i]))
    e.append(s[i])
    curr = i + 1
  elif i == len(s) - 1:
    e.append(int(s[curr:i + 1]))

f = add
for i, v in enumerate(e):
  if v == '-':
    f = sub
  elif v == '+':
    continue
  else:
    ans = f(ans, v)

print(ans)