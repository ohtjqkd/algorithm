k = int(input())
n = int(input())

i = 1
while True:
    if i >= n:
        break
    print(i)
    k -= i
    i += 1
print(k)