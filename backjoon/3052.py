visited = [0] * 42
count = 0
for _ in range(10):
    visited[int(input()) % 42] += 1
for v in visited:
    if v:
        count += 1
print(count)
