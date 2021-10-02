a, b = int(input()), int(input())

ret = str((b - ((a - (a % 100)) % b)) % b)
if len(ret) == 1:
    ret = "0"+ret
print(ret)

# input
# 1000
# 3