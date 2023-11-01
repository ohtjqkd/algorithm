def han(n):
    arr = list(map(int, list(str(n))))
    if len(arr) == 1:
        return True
    dif = arr[0] - arr[1]
    for i in range(2, len(arr)):
        if arr[0]-arr[i] == dif*i:
            continue
        else:
            return False
    return True


n = int(input())
count = 0
for i in range(1, n+1):
    if han(i):
        count += 1
print(count)
