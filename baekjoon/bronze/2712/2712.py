# input
# 5
# 1 kg
# 2 l
# 7 lb
# 3.5 g
# 0 l
# output
# 2.2046 lb
# 0.5284 g
# 3.1752 kg
# 13.2489 l
# 0.0000 g
convertor = {
    "kg": ["lb", 2.2046],
    "lb": ["kg", 0.4536],
    "l": ["g", 0.2642],
    "g": ["l", 3.7854]
}
for _ in range(int(input())):
    v, u = input().split(" ")
    t, cv = convertor[u]
    print(f'{cv * float(v):.4f} {t}')