# input: 11001100
# output: 314


binary = input()
i, ret, loc_value, exp = 0, 0, 0, 0
while len(binary)-i-1 >= 0:
    curr_idx = len(binary)-i-1
    loc_value += int(binary[curr_idx]) * (2**(i % 3))
    if i % 3 == 2:
        ret += loc_value * (10 ** exp)
        exp += 1
        loc_value = 0
    i += 1
if loc_value != 0:
    ret += loc_value * (10 ** exp)
print(ret)