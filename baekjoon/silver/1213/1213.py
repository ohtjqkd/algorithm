# input
# AABB
from collections import Counter
s = input()


dic = Counter(s)
def check_able(dic):
    cnt = 0
    odd_value = None
    for k, v in dic.items():
        if v % 2 == 1:
            cnt +=1
            odd_value = k
        if cnt > 1:
            return False, odd_value
    return True, odd_value

param = check_able(dic)
if not param[0]:
    print("I'm Sorry Hansso")
else:
    ret = ''
    if param[1]:
        ret = param[1]
        dic[param[1]] -= 1
    for k in sorted(dic.keys(), reverse=True):
        ret = k*(dic[k]//2) + ret + k*(dic[k]//2)

    print(ret)
