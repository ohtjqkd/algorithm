# input: 11001100
# output: 314


# binary = input()
# i, ret, loc_value, exp = 0, 0, 0, 0
# while len(binary)-i-1 >= 0:
#     curr_idx = len(binary)-i-1
#     loc_value += int(binary[curr_idx]) * (2**(i % 3))
#     if i % 3 == 2:
#         ret += loc_value * (10 ** exp)
#         exp += 1
#         loc_value = 0
#     i += 1
# if loc_value != 0:
#     ret += loc_value * (10 ** exp)
# print(ret)

# ret = []
# while b:
#     if len(b) > 3:
#         b, tmp = b[:-3], b[-3:]
#     else:
#         b, tmp = [], b
#     t = 0
#     for i in range(1, len(tmp)+1):
#         if tmp[-i] == '1':
#             t += 2**(i-1)
#     ret = [str(t)] + ret
# print(''.join(ret))

# b = int(input(), 2)
# print(b)
# ret = []
# while b > 0:
#     ret.append(str(b%8))
#     b //= 8
# print(''.join(reversed(ret)))

# 위에 코드랑 다른 점이 뭐지?
# slicing하면서 더 많은 연산이 필요한건가?
b = list(input())
ret =[]
b.reverse()
for i in range(0, len(b), 3):
    t = b[i:min(i+3, len(b))]
    s = 0
    for j in range(len(t)):
        if t[j] == '1':
            s += 2**j
    ret.append(str(s))
print(''.join(reversed(ret)))