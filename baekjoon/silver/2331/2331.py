# input: 57 2
# output: 4

A, P = map(int, input().split(" "))
is_exit = {}
node = A
ret = []
while is_exit.get(node) == None:
    ret.append(node)
    is_exit[node] = True
    next_node = 0
    while node > 0:
        next_node += (node % 10) ** P
        node //= 10
    node = next_node
while ret.pop() != node:
    pass
print(len(ret))

