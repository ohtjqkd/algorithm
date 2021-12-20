# input: A0
# output: 4.0

dictionary = dict(zip(list("FDCBA+-0"), [0.0, 1.0, 2.0, 3.0, 4.0, 0.3, -0.3, 0.0]))

s = input()
print(float(dictionary.get(s[0])+dictionary.get(s[-1], 0)))