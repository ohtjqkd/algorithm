# input
# 7 3

N, K = list(map(int, input().split(" ")))

ret = []
arr = [i+1 for i in range(N)]
idx = -1
while arr:
    idx = (idx+K) % len(arr)
    ret.append(arr[idx])
    del arr[idx]
    idx -= 1
print(str(ret).replace("[", "<").replace("]", ">"))

# deque 사용 근데 더 느림
# from collections import deque

# N, K = list(map(int, input().split(" ")))
# arr = deque([i+1 for i in range(N)])
# ret = []
# while arr:
#     for _ in range(K-1):
#         arr.append(arr.popleft())
#     ret.append(arr.popleft())
# print(f"<{', '.join(list(map(str, ret)))}>")
