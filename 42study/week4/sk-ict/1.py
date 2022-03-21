# 

def solution(money, cost):
    ret = 0
    cost = list(zip(cost, [1,5,10,50,100,500]))
    cost.sort(key=lambda x: (x[0]/x[1], x[1]))
    for c, v in cost:
        ret += (money // v * c)
        money %= v
        if money == 0:
            break
    return ret


T = [
    [4578, [1, 4, 99, 35, 50, 1000], 2308],
    [1999, [2, 11, 20, 100, 200, 600], 2798]
]

for t in T:
    print(t[2] == solution(t[0], t[1]))