
# test case가 부족해..
# 틀림
import sys


input = sys.stdin.readline
n = int(input())
L = [[] for _ in range(101)]
N = [0] * 100001

for i in range(n):
    num, rank = map(int, input().split(" "))
    L[rank].append(num)
    N[num] = rank

M = int(input())
for _ in range(M):
    line = input().rstrip().split(" ")
    com = line[0]
    if com == "add":
        num, rank = int(line[1]), int(line[2])
        L[rank].append(num)
        N[num] = rank
    elif com == "solved":
        num = int(line[1])
        L[N[num]].remove(num)
        N[num] = 0
    else:
        want = int(line[1])
        if want == -1:
            for i in range(1, 101):
                if L[i]:
                    L[i].sort()
                    print(L[i][0])
                    break
        elif want == 1:
            for i in range(100, 0, -1):
                if L[i]:
                    L[i].sort()
                    print(L[i][-1])
                    break
# added = False
# for _ in range(int(input())):
#     line = input().split(" ")
#     com = line[0]
#     if com == "add":
#         added = True
#         num, rank = int(line[1]), int(  line[2])
#     elif com == "solved":

#         if len(is_solved[int(line[1])]) != 0:
#             is_solved[int(line[1])].pop()
#     else:
#         want = int(line[1])
#         if want == -1:
#             while min_heap:
#                 rank, num = heapq.heappop(min_heap)
#                 # print(num, ":", is_solved[num])
#                 if rank in is_solved[num]:
#                     print(num)
#                     heapq.heappush(min_heap, (rank, num))
#                     break
#                 # print(min_heap)
#         elif want == 1:
#             while max_heap:
#                 rank, num = heapq.heappop(max_heap)
#                 # print(num, ":", is_solved[-num])
#                 if -rank in is_solved[-num]:
#                     print(-num)
#                     heapq.heappush(max_heap, (-rank, -num))
#                     break    
# max_heap = []
# min_heap = []
# is_solved = [set() for _ in range(100002)] 
# for i in range(N):
#     num, rank = map(int, input().split(" "))
#     heapq.heappush(min_heap, (rank, num))
#     heapq.heappush(max_heap, (-rank,-num))
#     is_solved[num].add(rank)
# for _ in range(int(input())):
#     line = input().split(" ")
#     com = line[0]
                    
    # print(is_solved)
    # print(min_heap)
    # print(max_heap)

            
