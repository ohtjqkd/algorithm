# input
# 5
# GOOD
# LUCK
# AND
# HAVE
# FUN
# 7
# output
# 31YUB

from functools import cmp_to_key

def transform(n: int):
  if n < 10:
    return str(n)
  else:
    return chr(ord('A') + n - 10)

def atoi(c: str):
  if c.isdigit():
    return ord(c) - ord('0')
  else:
    return ord(c) - ord('A') + 10

def itoa(n: int):
  if n < 10:
    return str(n)
  else:
    return chr(ord('A') + n - 10)

def sum_character(num: int, exp: int, t: list):
  t[exp] += num
  
def compare(a: tuple, b: tuple):
  for i in range(51, -1, -1):
    if a[1][i] == b[1][i]:
      continue
    return a[1][i] - b[1][i]
  return -1

n = int(input())
nums = []
sum_map = dict()
for _ in range(n):
  s = input()
  nums.append(s)
  for i, c in enumerate(reversed(s)):
    if sum_map.get(c) is None:
      sum_map[c] = [0 for _ in range(52)]
    sum_character(35 - atoi(c), i, sum_map[c])

k = int(input())

for key, v in sum_map.items():
  for i in range(51):
    d, v = divmod(sum_map[key][i], 36)
    sum_map[key][i] = v
    sum_map[key][i+1] += d

res = sorted(sum_map.items(), key=cmp_to_key(compare), reverse=True)
for i in range(len(nums)):
  for c, _ in res[:min(len(res), k)]:
    nums[i] = nums[i].replace(c, 'Z')
res = [0] * 52
for s in nums:
  for i, c in enumerate(reversed(s)):
    sum_character(atoi(c), i, res)

for i in range(51):
  d, res[i] = divmod(res[i], 36)
  res[i+1] += d

ans = ""
for i in range(51, -1, -1):
  if res[i] != 0:
    for j in range(i, -1, -1):
      ans = ans + transform(res[j])
    break
if ans == "":
  ans = "0"
print(ans)
