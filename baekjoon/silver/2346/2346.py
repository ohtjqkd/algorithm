# input
# 5
# 3 2 1 -3 -1
# output
# 1 4 5 3 2

from collections import deque

n = int(input())

# arr = deque(list(map(int, input().split())))

arr = list(map(int, input().split()))
arr = deque([(arr[i], i+1) for i in range(n)])

target = arr.popleft()
ans = [target[1]]
skip = target[0]
while arr:
  if skip < 0:
    skip = -skip
    while skip > 1:
      arr.appendleft(arr.pop())
      skip -= 1
    target = arr.pop()
    skip = target[0]
    ans.append(target[1])
  else:
    while skip > 1:
      arr.append(arr.popleft())
      skip -= 1
    target = arr.popleft()
    skip = target[0]
    ans.append(target[1])
print(' '.join(map(str, ans)))

