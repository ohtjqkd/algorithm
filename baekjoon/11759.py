import sys

input = sys.stdin.readline

s, v1, v2 = map(int, input().rstrip().split(" "))

mapping = {1: max(v1, v2), 0: min(v1, v2)}

for i in range(s // mapping[1], -1, -1):
    mod = (s - (mapping[1] * i))
    if mod % mapping[0] == 0:
        if v1 > v2:
            print(i, mod // mapping[0])
        else:
            print(mod // mapping[0], i)
        break
else:
    print("Impossible")