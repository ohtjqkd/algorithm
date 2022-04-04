from bisect import bisect, bisect_right, insort
from collections import deque, defaultdict
import difflib
from multiprocessing.connection import wait
import sys
input = sys.stdin.readline
write = sys.stdout.write
# test case가 부족해..
# 틀림

from collections import defaultdict
import sys
import heapq

si = sys.stdin.readline
def MIIS(): return map(int, si().split())


n = int(si())

min_heap = []
max_heap = []
diff_heap = [[[], []] for _ in range(101)]
algo_heap = [[[], []] for _ in range(101)]
ret = []
num_list = [[0,0] for _ in range(100001)]
visited = defaultdict()

for _ in range(n):
    num, difficulty, algo_num = MIIS()
    heapq.heappush(min_heap, (difficulty, num, algo_num))
    heapq.heappush(max_heap, (-difficulty, -num, -algo_num))
    heapq.heappush(algo_heap[algo_num][0], (difficulty, num, algo_num))
    heapq.heappush(algo_heap[algo_num][1], (-difficulty, -num, -algo_num))
    heapq.heappush(diff_heap[difficulty][0], (difficulty, num, algo_num))
    heapq.heappush(diff_heap[difficulty][1], (-difficulty, -num, -algo_num))

    visited[num] = [difficulty, algo_num]
m = int(si())
for _ in range(m):
    line = si().split()
    if line[0] == 'add':
        num, difficulty, algo_num = map(int, line[1:])
        heapq.heappush(min_heap, (difficulty, num, algo_num))
        heapq.heappush(max_heap, (-difficulty, -num, -algo_num))
        heapq.heappush(algo_heap[algo_num][0], (difficulty, num, algo_num))
        heapq.heappush(algo_heap[algo_num][1], (-difficulty, -num, -algo_num))
        heapq.heappush(diff_heap[difficulty][0], (difficulty, num, algo_num))
        heapq.heappush(diff_heap[difficulty][1], (-difficulty, -num, -algo_num))        
        visited[num] = [difficulty, algo_num]

    elif line[0] == 'solved':
        visited[int(line[1])] = [0, 0]
    elif line[0] == 'recommend2':
        if line[1] == '1':
            while max_heap:
                diff, num, algo_num = max_heap[0]
                if visited[-num][0] == -diff and visited[-num][1] == -algo_num:
                    ret.append(-num)
                    break
                heapq.heappop(max_heap)
        elif line[1] == '-1':
            while min_heap:
                diff, num, algo_num = min_heap[0]
                if visited[num][0] == diff and visited[num][1] == algo_num:
                    ret.append(num)
                    break
                heapq.heappop(min_heap)

    elif line[0] == 'recommend':
        algo_num, want = map(int, line[1:])
        if want == 1:
            while algo_heap[algo_num][1]:
                diff, num, t_algo_num = algo_heap[algo_num][1][0]
                if visited[-num][0] == -diff and visited[-num][1] == -t_algo_num:
                    ret.append(-num)
                    break
                heapq.heappop(algo_heap[algo_num][1])
        elif want == -1:
            while algo_heap[algo_num][0]:
                diff, num, t_algo_num = algo_heap[algo_num][0][0]
                if visited[num][0] == diff and visited[num][1] == t_algo_num:
                    ret.append(num)
                    break
                heapq.heappop(algo_heap[algo_num][0])
    elif line[0] == 'recommend3':
        want, l = map(int, line[1:])
        if want == 1:
            for i in range(l, 101):
                check = False
                while diff_heap[i][1]:
                    diff, num, algo_num = diff_heap[i][1][0]
                    if visited[-num][0] == -diff and visited[-num][1] == -algo_num:
                        ret.append(-num)
                        check =True
                        break
                    heapq.heappop(diff_heap[i][1])
                if check:
                    break
            else:
                ret.append(-1)
        if want == -1:
            for i in range(l, 0, -1):
                check = False
                while diff_heap[i][0]:
                    diff, num, algo_num = diff_heap[i][0][0]
                    if visited[num][0] == diff and visited[num][1] == algo_num:
                        ret.append(num)
                        check =True
                        break
                    heapq.heappop(diff_heap[i][0])
                if check:
                    break
            else:
                ret.append(-1)

for ans in ret:
    print(ans)




# N = int(input())

# where_number = [0] * 100001
# command = []
# init_pair = []
# total_pair = []

# diff_list = [[] for _ in range(101)]
# algo_list = [[] for _ in range(101)]
# num_list = [[0, 0] for _ in range(100001)]
# most_min = float('inf')
# most_max = float('-inf')
# for i in range(N):
#     num, dif, algo_num = map(int, input().split(" "))
#     num_list[num] = [dif, algo_num]
#     insort(algo_list[algo_num], (dif, num))
#     insort(diff_list[dif], num)
#     most_min = min(most_min, dif)
#     most_max = max(most_max, dif)

# # print(algo_list)
# M = int(input())

# for i in range(M):
#     # print()
#     # print()
#     line = input().rstrip().split(" ")
#     com = line[0]
#     # print(i, "th command: ", com, line[1:])

#     if com == "add":
#         num, dif, algo_num = map(int, line[1:])
#         insort(algo_list[algo_num], (dif, num))
#         insort(diff_list[dif], num)
#         num_list[num] = [dif, algo_num]
#         most_min = min(most_min, dif)
#         most_max = max(most_max, dif)
#         # print("most_min ", most_min, " most_max ", most_max)

#     elif com == "solved":
#         num = int(line[1])
#         dif, algo_num = num_list[num][0], num_list[num][1]
#         # print("now dif ", dif, " now algo num ", algo_num)
#         idx = bisect_right(algo_list[algo_num], (dif, num))
#         # print("algo_list", algo_list, "idx", idx)

#         del(algo_list[algo_num][idx-1])
#         idx = bisect_right(diff_list[dif], num)
#         del(diff_list[dif][idx-1])
#         if dif == most_min and len(diff_list[dif]) == 0:
#             for i in range(dif, 101):
#                 if len(diff_list[i]) != 0:
#                     most_min = i
#                     break
#             else:
#                 most_min = float('inf')
#         if dif == most_max and len(diff_list[dif]) == 0:
#             for i in range(dif, 0, -1):
#                 if len(diff_list[i]) != 0:
#                     most_max = i
#                     break
#             else:
#                 most_max = float('-inf')
#         # print("most_min ", most_min, " most_max ", most_max)
#         num_list[num][0], num_list[num][1] = 0, 0
#     elif com == "recommend":
#         algo_num, want = map(int, line[1:])
#         if want == -1:
#             print(algo_list[algo_num][0][1])
#         else:
#             print(algo_list[algo_num][-1][1])
#     elif com == "recommend2":
#         want = int(line[1])
#         if want == -1:
#             print(diff_list[most_min][0])
#         else:
#             print(diff_list[most_max][-1])
#     elif com == "recommend3":
#         want, l = map(int, line[1:])
#         if want == -1:
#             for i in range(l, most_min - 1 , -1):
#                 if len(diff_list[i]) != 0:
#                     print(diff_list[i][-1])
#                     break
#             else:
#                 print(-1)
#         else:
#             for i in range(l, most_max + 1):
#                 if len(diff_list[i]) != 0:
#                     print(diff_list[i][0])
#                     break
#             else:
#                 print(-1)
    # print("algo_list")
    # print(algo_list)
    # print("diff_list")
    # print(diff_list)