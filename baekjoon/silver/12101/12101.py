
global n
global k
global count


def dfs(a: list, s: int):
    global k
    global count
    global n

    if s == n:
        count += 1
        if count == k:
            return True
        return False
    for i in [1, 2, 3]:
        if s + i > n:
            continue
        a.append(i)
        if dfs(a, s + i):
            return True
        else:
            a.pop()
    return False

n, k = map(int, input().split(" "))

count = 0
a = []            
dfs(a, 0)

if a == []:
    print(-1)
else:
    print("+".join(map(str, a)))