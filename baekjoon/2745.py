# input: ZZZZZ 36
# output: 60466175
ret = 0
order = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
n_str, d = input().split(" ")
d = int(d)
order = dict(zip(order[:d], range(d)))

for i in range(1, len(n_str)+1):
    ret += order.get(n_str[-i]) * (d**(i-1))
print(ret)