# input
# 2
# 3
# Fred Barney
# Barney Betty
# Betty Wilma
# 3
# Fred Barney
# Betty Wilma
# Barney Betty

# output
# 2
# 3
# 4
# 2
# 2
# 4

def solution():
    def find(name, parent: dict):
        if parent.get(name) == name:
            return name
        parent[name] = find(parent.get(name), parent)
        return parent[name]
    TC = int(input())

    for _ in range(TC):
        argc = int(input())
        parent = dict()
        network = dict()
        for _ in range(argc):
            name_1, name_2 = input().split(" ")
            if parent.get(name_1) == None:
                parent[name_1] = name_1
                network[name_1] = 1
            if parent.get(name_2) == None:
                parent[name_2] = name_2
                network[name_2] = 1
            root_1, root_2 = find(name_1, parent), find(name_2, parent)
            if root_1 == root_2:
                print(network.get(root_1))
            else:
                network[root_1] += network[root_2]
                parent[root_2] = root_1
                print(network[root_1])
            

solution()        