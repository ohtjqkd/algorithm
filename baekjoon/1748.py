N = input()
ret = 0
for i in range(len(N)):
    ret += (i+1) * (min(int(N), 10**(i+1))-10**i)+1
print(ret)