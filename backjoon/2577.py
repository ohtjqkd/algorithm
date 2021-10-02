a, b, c = int(input()), int(input()), int(input())
count = [0] * 10
mul = a*b*c
while mul > 10:
    count[mul % 10] += 1
    mul //= 10
count[mul] += 1
for c in count:
    print(c)
