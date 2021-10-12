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

# input
# 7 3