from collections import defaultdict

def solution(enroll, referral, seller, amount):
    benefits = defaultdict(int)
    for name, a in zip(seller, amount):
        benefits[name] = a * 100
    child_tree, parent_tree = make_tree(enroll, referral)
    dfs("-", benefits, child_tree, parent_tree)
    answer = [benefits.get(name, 0) for name in enroll]
    return answer

def make_tree(enroll, referral):
    child_tree = defaultdict(list)
    parent_tree = dict()
    for r, e in list(zip(referral, enroll)):
        child_tree[r].append(e)
        parent_tree[e] = r
    return (child_tree, parent_tree)

def dfs(node, benefits, child_tree, parent_tree):
    children_nodes = child_tree.get(node, None)
    parent_node = parent_tree.get(node, None)
    curr_benefit = benefits.get(node, None)
    while parent_node:
        if parent_node != None and curr_benefit != None and curr_benefit >= 10:
            benefits[parent_node] += round(curr_benefit * 0.1)
            benefits[node] -= round(curr_benefit * 0.1)
        node = parent_node
        curr_benefit = benefits.get(node, None)
    if children_nodes != None:
        for c in children_nodes:
            dfs(c, benefits, child_tree, parent_tree)

test_case = [
    [
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10],
        [360, 958, 108, 0, 450, 18, 180, 1080]
    ],
    [
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["sam", "emily", "jaimie", "edward"],
        [2, 3, 5, 4],
        [0, 110, 378, 180, 270, 450, 0, 0]
    ]
]

print(solution(test_case[0][0],test_case[0][1],test_case[0][2],test_case[0][3]))
print(solution(test_case[1][0],test_case[1][1],test_case[1][2],test_case[1][3]))
