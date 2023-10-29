# input
# 5
# 1 1 1 1 1
# 1 2 3 4 5
# 3
# 1 3 5
# output
# 1 3 5

n = int(input())

t = list(map(int, input().split()))

v = list(map(int, input().split()))

m = int(input())

q = []
for i in range(n - 1, -1, -1):
  if t[i] == 0:
    q.append(v[i])
    
inp = list(map(int, input().split()))

ret = []
for i in inp:
  q.append(i)

print(' '.join(list(map(str, q[:m]))))