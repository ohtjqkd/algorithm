a, b = input().split()
da, db = '', ''
for i in range(2, -1, -1):
    da += a[i]
    db += b[i]
for i in range(3):
    if da[i] > db[i]:
        print(da)
        break
    elif da[i] < db[i]:
        print(db)
        break
