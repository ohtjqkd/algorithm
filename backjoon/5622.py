string = input()
alpha_v = "22233344455566677778889999"
time = 0
for i in string:
    time += int(alpha_v[ord(i)-65])+1

print(time)
