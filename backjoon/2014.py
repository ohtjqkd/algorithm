import heapq as hq
import copy

K, N = map(int, input().split(" "))

p_list = list(map(int, input().split(" ")))

lst, ck = copy.deepcopy(p_list), set()

hq.heapify(lst)

ith = 0
mn = 0

while ith < N:
    mn = hq.heappop(lst)
    if mn in ck:
        continue
    ith += 1
    ck.add(mn)
    for prime in p_list:
        if mn * prime < 2 ** 32:
            hq.heappush(lst, mn*prime)

print(mn)
