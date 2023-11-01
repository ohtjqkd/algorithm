# input
# 14
# output
# 2/4

x = int(input())
i = 0
while True:
    if i*(i+1)//2 >= x and i*(i-1)//2 < x:
        break
    i += 1
step = x-i*(i-1)//2
if i % 2 == 0:
    print(str(step)+"/"+str(i-step+1))
else:
    print(str(i-step+1)+"/"+str(step))
