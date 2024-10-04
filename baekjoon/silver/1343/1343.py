def replace_poly(n: int) -> str:
  ret: str = ''
  if n % 2 == 1:
    return ret
  for _ in range(n//4):
    ret += 'AAAA'
  n %= 4
  for _ in range(n//2):
    ret += 'BB'
  return ret

sp = list()
cc = 0
s = input()
for i in range(1, len(s)+1):
  if i < len(s) and s[i] == s[cc]:
    continue
  sp.append(s[cc:i])
  cc = i

for i, v in enumerate(sp):
  if v[0] == 'X':
    sp[i] = replace_poly(len(v))
    if sp[i] == '':
      print(-1)
      break
else:
  print(''.join(sp))