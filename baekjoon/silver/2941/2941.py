change = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

string = input()

count = 0

for i in range(len(change)):
    string = string.replace(change[i], str(i))
print(len(string))
