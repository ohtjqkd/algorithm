count = 0
for i in range(int(input())):
    string = input()
    visited = [0]*26
    init_c = string[0]
    visited[ord(init_c)-97] = 1
    grouped = True
    for c in string:
        if c == init_c:
            continue
        else:
            if not visited[ord(c)-97]:
                visited[ord(c)-97] = 1
                init_c = c
            else:
                grouped = False
                break
    if grouped:
        count += 1

print(count)
