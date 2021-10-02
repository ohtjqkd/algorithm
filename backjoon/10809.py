string = input()
visited = [-1] * 26
for idx, c in enumerate(string):
    if visited[ord(c)-97] == -1:
        visited[ord(c)-97] = idx
for v in visited:
    print(v, end=' ')
