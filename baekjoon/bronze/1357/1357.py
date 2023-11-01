# input: 123 100, 111 111, 5 5, 1000 1, 456 789
# output: 223, 222, 1, 2, 1461

def rev(s):
    s = str(s)
    ret = 0
    len_s = len(s)
    for i in range(len_s):
        ret += int(s[i]) * (10 ** i)
    return ret

x, y = input().split()
print(rev(rev(x)+rev(y)))