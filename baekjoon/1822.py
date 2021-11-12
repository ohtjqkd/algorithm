# input
# 4 3
# 2 5 11 7
# 9 7 4
# output
# 3
# 2 5 11
from collections import deque
a_n, b_n = map(int, input().split(" "))
A = deque(sorted(list(map(int, input().split(" ")))))
B = deque(sorted(list(map(int, input().split(" ")))))
# a_tri = {}
# for a in A:
#     node = a_tri
#     for i in a:
#         if node.get(i) == None:
#             node[i] = {}
#         node = node[i]
#     node['end'] = {}
ret = []
while A and B:
    if A[0] == B[0]:
        A.popleft()
        B.popleft()
    elif A[0] > B[0]:
        B.popleft()
    else:
        ret.append(A.popleft())
ret = list(map(str, ret+list(A)))
print(len(ret))
print(' '.join(ret))

# print(a_tri)
