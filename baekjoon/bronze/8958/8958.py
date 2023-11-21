n = int(input())
for _ in range(n):
    oxs = list(input())
    total, step = 0, 1
    for d in oxs:
        if d == 'O':
            total += step
            step += 1
        else:
            step = 1
    print(total)
