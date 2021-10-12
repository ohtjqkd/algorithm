string = input()
visit_c = [0] * 26
result = []
for c in string:
    C = c.upper()
    visit_c[ord(C)-65] += 1
max_v = max(visit_c)
for idx, c in enumerate(visit_c):
    if max_v == c:
        result.append(idx)

if len(result) > 1:
    print("?")
else:
    print(chr(result[0]+65))
