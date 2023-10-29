# input
# 3
# 10010111
# 011000100110001
# 0110001011001
# output
# NO
# NO
# YES

import sys, re

input = sys.stdin.readline

p = re.compile('^(100+1+|01)+$')
for i in range(int(input())):
  s = input().strip()
  if p.match(s):
    print('YES')
  else:
    print('NO')