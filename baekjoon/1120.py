a, b = input().split(" ")
ret = 0
for i in range(len(b)-len(a)+1):
    same_cnt = 0
    for j in range(len(a)):
        if a[j] == b[i+j]:
            same_cnt += 1
    ret = max(ret, same_cnt)

print(len(a)-ret)

# input
# adaabc aababbc