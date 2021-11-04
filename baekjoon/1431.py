#input 
# 5
# ABCD
# 145C
# A
# A910
# Z321
# output
# A
# ABCD
# Z321
# 145C
# A910

def sum_int(serial):
    ret = 0
    for s in serial:
        try:
            ret += int(s)
        except:
            pass
    return ret

N = int(input())
serial_li = [input() for _ in range(N)]
serial_li.sort(key=lambda x: (len(x), sum_int(x), x))
for s in serial_li:
    print(s)