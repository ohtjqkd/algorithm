# input
# 4
# 1
# 3
# 7
# 13
# output
# 3
n = int(input())

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

prev_value = int(input())
already_tree = [prev_value]
dist = set()
for i in range(n - 1):
  curr_value = int(input())
  already_tree.append(curr_value)
  dist.add(curr_value - prev_value)
  prev_value = curr_value

dist = list(dist)
a = dist[0]
for i in range(1, len(dist)):
  a = gcd(a, dist[i])
print((already_tree[-1] - already_tree[0]) // a - n + 1)