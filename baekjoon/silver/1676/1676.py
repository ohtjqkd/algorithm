two = 0
five = 0
for i in range(2, int(input())+1):
    while i % 2 == 0:
        i //= 2
        two += 1
    while i % 5 == 0:
        i //= 5
        five += 1
print(min(two, five))
    
