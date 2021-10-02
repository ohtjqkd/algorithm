idx, max_v = 0, 0
for i in range(9):
    n = int(input())
    if n > max_v:
        max_v, idx = n, i+1

print(max_v)
print(idx)
