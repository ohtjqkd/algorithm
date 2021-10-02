from collections import defaultdict

sales, links = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [
    [10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
# sales, links = [10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]]

nodes = defaultdict(list)
dp = []
gsales = []


def recursive(node):
    global nodes
    global dp
    global gsales
    children = nodes.get(node)
    if not children:
        dp[node-1][1] = gsales[node-1]
        return
    for child in children:
        recursive(child)
    chkNode = [child for child in children if dp[child-1]
               [0] > dp[child-1][1]]
    sum_children = sum(min(dp[child-1][1], dp[child-1][0])
                       for child in children)
    dp[node-1][1] = sales[node-1] + sum_children
    if chkNode:
        dp[node-1][0] = sum_children
    else:
        dp[node-1][0] = sum_children + \
            min([dp[child-1][1]-dp[child-1][0]
                 for child in children])
    return


def solution(sales, links):
    global nodes
    global dp
    global gsales
    gsales = sales
    dp = [[0, 0] for _ in range(len(sales))]
    for link in links:
        lead, sub = link
        nodes[lead].append(sub)
    recursive(1)
    return min(dp[0][0], dp[0][1])


# def solution(sales, links):
#     answer = 0
#     nodes = defaultdict(list)
#     dp = [[0, 0] for _ in range(len(sales))]
#     for link in links:
#         lead, sub = link
#         nodes[lead].append(sub)
#     layer_ordered, stack = [[1]], [[1]]
#     while stack:
#         tmp = []
#         layer = stack.pop()
#         for node in layer:
#             if nodes.get(node):
#                 tmp.extend(nodes[node])
#         if tmp:
#             layer_ordered.append(tmp)
#             stack = [tmp]
#     while layer_ordered:
#         layer = layer_ordered.pop()
#         for node in layer:
#             if not nodes.get(node):
#                 dp[node-1][0], dp[node-1][1] = 0, sales[node-1]
#                 continue
#             childrenNode = nodes[node]
#             chkNode = [child for child in childrenNode if dp[child-1]
#                        [0] > dp[child-1][1]]
#             sum_children = sum(min(dp[child-1][1], dp[child-1][0])
#                                for child in childrenNode)
#             dp[node-1][1] = sales[node-1] + sum_children
#             if chkNode:
#                 dp[node-1][0] = sum_children
#             else:
#                 dp[node-1][0] = sum_children + \
#                     min([dp[child-1][1]-dp[child-1][0]
#                          for child in childrenNode])
#         print(dp)
#     return min(dp[0][0], dp[0][1])
# class Team:
#     def __init__(self, leader=None):
#         self.leader = leader
#         self.sub = {}
#     def getSub(self):
#         return self.sub
# def solution(sales, links):
#     dp = [[0 if i == 0 else sales[j]
#            for i in range(2)] for j in range(len(sales))]
#     # print(dp)
#     org = defaultdict(Team)
#     for link in links:
#         leader, sub = link
#         # print(org[leader])
#         org[leader].leader = leader
#         if not org.get(sub):
#             org[sub] = Team(sub)
#         org[leader].getSub()[sub] = org[sub]
#     dept = [[org[1]]]
#     stack = [[org[1]]]
#     # print(org)
#     while len(stack) != 0:
#         tmp = []
#         layer = stack.pop()
#         for i in layer:
#             tmp.extend(i.sub.values())
#         if tmp:
#             stack.append(tmp)
#             dept.append(tmp)
#         # for t in tmp:
#             # print(t.leader)
#     # print(dept)
#     while dept:
#         teams = dept.pop()
#         for team in teams:
#             root, children = team.leader, team.sub.values()
#             if not children:
#                 continue
#             sum_child = sum(
#                 [min(dp[child.leader-1][0], dp[child.leader-1][1]) for child in children])
#             print(sum_child)
#             dp[root-1][1] = sales[root-1] + sum_child
#             # if there is no one, dp[k][0] > dp[k][1] in children node
#             minValue = min([dp[child.leader-1][1]-dp[child.leader-1][0] if dp[child.leader-1]
#                             [1] > dp[child.leader-1][0] else [0] for child in children])
#             dp[root-1][0] = sum_child + minValue
#             # print(sum_child)
#             # dp[root][1] =
#             # dp[team.leader][0] = min([dp[i.leader][1]
#             #   for i in team.sub.values()] if team.sub.values() else [dp[team.leader][1]])
#     return min(dp[0][0], dp[0][1])
print(solution(sales, links))
