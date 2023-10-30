# input
# 8
# 4 1 6 1 3 6 1 4
# output
# 4 0 6 1 3 7 2 5

# B[p[i]] = A[i]
from collections import defaultdict, deque
n = int(input())
idx_map = defaultdict(deque)
A = list(map(int, input().split()))
B = sorted(A)
for idx, a in enumerate(B):
  idx_map[a].append(idx)
  
print(idx_map)
ret = [str(idx_map[a].popleft()) for a in A]
print(' '.join(ret))