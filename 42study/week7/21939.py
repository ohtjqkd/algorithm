
# test case가 부족해..
# 틀림
import sys, heapq

input = sys.stdin.readline
N = int(input())
max_heap = []
min_heap = []
is_solved = [set() for _ in range(100002)] 
for i in range(N):
    num, rank = map(int, input().split(" "))
    heapq.heappush(min_heap, (rank, num))
    heapq.heappush(max_heap, (-rank,-num))
    is_solved[num].add(rank)
for _ in range(int(input())):
    line = input().split(" ")
    com = line[0]
    if com == "add":
        num, rank = int(line[1]), int(  line[2])
        is_solved[num].add(rank)
        heapq.heappush(min_heap, (rank, num))
        heapq.heappush(max_heap, (-rank, -num))
    elif com == "solved":
        if len(is_solved[int(line[1])]) != 0:
            is_solved[int(line[1])].pop()
    else:
        want = int(line[1])
        if want == -1:
            while min_heap:
                rank, num = heapq.heappop(min_heap)
                # print(num, ":", is_solved[num])
                if rank in is_solved[num]:
                    print(num)
                    heapq.heappush(min_heap, (rank, num))
                    break
                # print(min_heap)
        elif want == 1:
            while max_heap:
                rank, num = heapq.heappop(max_heap)
                # print(num, ":", is_solved[-num])
                if -rank in is_solved[-num]:
                    print(-num)
                    heapq.heappush(max_heap, (-rank, -num))
                    break
                    
    # print(is_solved)
    # print(min_heap)
    # print(max_heap)

            
