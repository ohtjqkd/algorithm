import datetime

# n = input()
# ret = []
# n = int(n, 8)
# n = bin(n)[2:]
# print(n)

n = input()
ret = []
mapping = {'0': '000', '1':'001', '2':'010', '3':'011', '4': '100', '5': '101', '6': '110', '7': '111'}
b = mapping.get(n[0])
for i in range(2):
    if b[i] != '0':
        ret.append(b[i:])
        break
else:
    ret.append(b[2])
for i in range(1, len(n)):
    ret.append(mapping.get(n[i]))
print(''.join(ret))
# while n > 0:
#     ret.append(mapping[n%10])
#     n //= 10
# ret = ''.join(list(reversed(ret)))
# for i in range(len(ret)):
#     if ret[i] == '1':
#         ret = ret[i:]
#         break

# input
# 314
