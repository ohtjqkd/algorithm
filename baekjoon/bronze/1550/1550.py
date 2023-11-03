ret = 0
hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
map = dict(zip(hex, range(16)))
hex_n = input()
for i, n in enumerate(hex_n):
    ret += 16 ** (len(hex_n)-1-i) * map[n]
print(ret)