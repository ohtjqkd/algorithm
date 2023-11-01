# input: 1236, 1, 1221, 4729382, 42393338
# output: YES, NO, YES, NO, YES

N = list(map(int, list(input())))
left_value, right_value = 1, 1
zero_idx = []
for i, n in enumerate(N):
    if n == 0:
        zero_idx.append(i)
    right_value *= n
for i in range(len(N)-1):
    if len(zero_idx) == 1:
        print("NO")
        break
    if len(zero_idx) > 1:
        print("YES")
        break
    left_value *= N[i]
    right_value //= N[i]
    if left_value == right_value:
        print("YES")
        break
else:
    print("NO")