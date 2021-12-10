# input: WrongAnswer
# output: wRONGaNSWER

p = list(input())
for i in range(len(p)):
    if p[i].islower():
        p[i] = p[i].upper()
    else:
        p[i] = p[i].lower()
print(''.join(p))