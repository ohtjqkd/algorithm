from collections import defaultdict
from itertools import combinations
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]


# def queryParser(result, queries):
#     ret = 0
#     queries = queries.split(" ")
#     need_visit = list(result.values(
#     )) if queries[0] == "-" else [result.get(queries[0])]
#     for idx, query in enumerate(queries):
#         tmp = []
#         if idx == 0:
#             continue
#         if query == "and":
#             continue
#         if idx == len(queries) - 1:
#             query = int(query)
#         # print("need_visit", need_visit)
#         while need_visit:
#             node = need_visit.pop()
#             # print("node", node)
#             if type(query) == int:
#                 tmp.append(node)
#                 continue
#             elif query == "-":
#                 # print("all next node", node.values())
#                 tmp.extend(list(node.values()))
#                 # print(tmp)
#             else:
#                 # print(f"next {query} {node.get(query)}")
#                 if node.get(query):
#                     tmp.append(node.get(query))
#         need_visit = tmp
#         # print(query)
#     for dic in need_visit:
#         for data in dic.items():
#             if data[0] >= query:
#                 ret += data[1]
#     return ret


# def solution(info, query):
#     result = {}
#     answer = []
#     # init data
#     for i in info:
#         node = result
#         i = i.split(" ")
#         i[-1] = int(i[-1])
#         for idx, t in enumerate(i):
#             if not node.get(t) and type(t) == int:
#                 node[t] = 0
#             elif not node.get(t):
#                 node[t] = {}
#             if type(t) == int:
#                 node[t] += 1
#             else:
#                 node = node[t]
#     # print(result)
#     # for i in result.values():
#     #     print(i)
#     for idx, q in enumerate(query):
#         answer.append(queryParser(result, q))

#     return answer


def getGreater(arr, targetNum):
    # print(arr, targetNum)
    mins, maxs = 0, len(arr)
    # print("need parsed", arr, targetNum)
    while mins < maxs:
        # print()
        mid = (maxs+mins)//2
        # print("from mins to maxs", arr[mins:maxs], [
        #   mins, maxs], "now mid value", arr[mid])
        if arr[mid] >= targetNum:
            maxs = mid
        else:
            mins = mid+1
    mid = (maxs + mins) // 2 if (maxs + mins) // 2 != -1 else 0
    return len(arr)-mid


def solution(info, query):

    # combs = []
    # for i in range(1, 5):
    #     combs.extend(combinations(range(4), i))
    # print(combs)
    answer = []
    result = defaultdict(list)
    for i in info:
        i = i.split(" ")
        targetNum = int(i[-1])
        for l in [i[0], "-"]:
            for s in [i[1], "-"]:
                for p in [i[2], "-"]:
                    for f in [i[3], "-"]:
                        fullQuery = l+s+p+f
                        result[fullQuery].append(targetNum)

        # print(i)
        # infoQuery = " ".join(i[:-1])
        # result[infoQuery].append(targetNum)
    for scores in result.values():
        scores.sort()
    memset = {}

    for idx, q in enumerate(query):
        # print(f"{idx+1}th query")
        totalCnt = 0
        q = q.split(" ")
        targetScore = int(q[-1])
        nowQuery = ""
        q = q[:-1]
        for i in q:
            if i != "and":
                nowQuery += i
        # nowQuery = "".join(q[:-1])
        # if memset.get(nowQuery):
        #     candArr = memset.get(nowQuery)
        # else:
        #     cand = list(result.keys())
        #     for type in q:
        #         if type == "and" or type == "-":
        #             continue
        #         tmp = []
        #         for c in cand:
        #             if type == "-" or type in c:
        #                 tmp.append(c)
        #         cand = tmp
        #     candArr = []
        #     for c in cand:
        #         candArr.extend(result[c])
        #     candArr.sort()
        #     memset[nowQuery] = candArr

        totalCnt += getGreater(result[nowQuery], targetScore)
        answer.append(totalCnt)
    return answer


print(solution(info, query))
