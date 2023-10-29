# input
# mobitel
# output
# bometil

s = list(input())
r_s = ''.join(reversed(s))
ret = ''
for i in range(2, 0, -1):
  cand = []
  for j in range(i, len(r_s)):
    cand.append(r_s[j:])
  cand.sort()
  ret += cand[0]
  r_s = r_s[:len(r_s) - len(cand[0])]
ret += r_s
print(ret)