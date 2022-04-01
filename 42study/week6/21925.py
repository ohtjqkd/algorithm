# 짝수 팰린드롬

# ... 이...이게 왜 되지??
from collections import deque

ret = 0
N = int(input())
A = deque(list(map(int, input().split(" "))))
prev = []
while len(A) > 1:
    flag = True
    if A[0] == A[1]:
        if len(A) - 2 < len(prev):
            ret = -1
            break
        for i in range(len(prev)):
            if prev[-i-1] != A[i+2]:
                flag = False
                break
        if flag:
            ret += 1
            for i in range(len(prev) + 2):
                A.popleft()
            prev = []
        else:
            prev.append(A.popleft())
    else:
        prev.append(A.popleft())
if ret == 0:
    ret = -1
print(ret)