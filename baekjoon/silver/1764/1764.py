# input
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton
# output
# 2
# baesangwook
# ohhenrie

N, M = map(int, input().split(" "))
tri = {}
ret = []
for i in range(N):
    hear = input()
    node = tri
    for h in hear:
        if node.get(h) == None:
            node[h] = {}
        node = node[h]
    node['end'] = {}
for j in range(M):
    see = input()
    node = tri
    for s in see:
        if node.get(s) == None:
            break
        node = node[s]
    else:
        if node.get('end') != None:
            ret.append(see)
ret.sort()
print(len(ret))
for r in ret:
    print(r)
