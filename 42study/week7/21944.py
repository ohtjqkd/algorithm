import sys, heapq

si = sys.stdin.readline
def MIIS(): return map(int, si().rstrip().split(" "))

class CurrentInfo:
    def __init__(self):
        self.num_list = [[0 for _ in range(2)] for _ in range(100001)]
    
    def solve(self, num):
        self.num_list[num][0], self.num_list[num][1] = 0, 0
    
    def add(self, num, diff, algo_num):
        if self.num_list[num][0] == 0 and self.num_list[num][1] == 0:
            self.num_list[num][0], self.num_list[num][1] = diff, algo_num
        else:
            return False
        return True
    
    def is_in_heap(self, heap_info, searching_type):
        diff, num, algo_num = map(lambda x: x * -searching_type, heap_info)
        if self.num_list[num][0] == diff and self.num_list[num][1] == algo_num:
            return True
        return False

class Recommend1:
    def __init__(self, limit = 100, info = CurrentInfo):
        self.info = info
        self.limit = limit
        self.max_heap = [[] for _ in range(self.limit + 1)]
        self.min_heap = [[] for _ in range(self.limit + 1)]
    
    def push(self, num, diff, algo_num):
        heapq.heappush(self.max_heap[algo_num], (-diff, -num, -algo_num))
        heapq.heappush(self.min_heap[algo_num], (diff, num, algo_num))

    def get_num_by_algo(self, algo_num, searching_type):
        if searching_type == 1:
            target_heap = self.max_heap[algo_num]
        elif searching_type == -1:
            target_heap = self.min_heap[algo_num]
        while target_heap:
            if self.info.is_in_heap(target_heap[0], searching_type):
                return -searching_type * target_heap[0][1]
            heapq.heappop(target_heap)

class Recommend2:
    def __init__(self, limit = 100001, info = CurrentInfo):
        self.info = info
        self.limit = limit
        self.max_heap = []
        self.min_heap = []
    
    def push(self, num, diff, algo_num):
        heapq.heappush(self.max_heap, (-diff, -num, -algo_num))
        heapq.heappush(self.min_heap, (diff, num, algo_num))

    def get_num(self, searching_type):
        if searching_type == 1:
            target_heap = self.max_heap
        elif searching_type == -1:
            target_heap = self.min_heap
        while target_heap:
            if self.info.is_in_heap(target_heap[0], searching_type):
                return -searching_type * target_heap[0][1]
            heapq.heappop(target_heap)

class Recommend3:
    def __init__(self, limit = 100, info = CurrentInfo):
        self.info = info
        self.limit = limit
        self.max_heap = [[] for _ in range(self.limit + 1)]
        self.min_heap = [[] for _ in range(self.limit + 1)]
    
    def push(self, num, diff, algo_num):
        heapq.heappush(self.max_heap[diff], (-diff, -num, -algo_num))
        heapq.heappush(self.min_heap[diff], (diff, num, algo_num))

    def get_num_from_diff(self, diff, searching_type):
        if searching_type == 1:
            target_heap = self.min_heap
        elif searching_type == -1:
            target_heap = self.max_heap
        while 0 <= diff < self.limit + 1:
            while target_heap[diff]:
                if self.info.is_in_heap(target_heap[diff][0], -searching_type):
                    return searching_type * target_heap[diff][0][1]
                heapq.heappop(target_heap[diff])
            diff += searching_type
        return -1

n = int(si())

info = CurrentInfo()
recom_1 = Recommend1(info = info)
recom_2 = Recommend2(info = info)
recom_3 = Recommend3(info = info)

for _ in range(n):
    num, difficulty, algo_num = MIIS()
    if info.add(num, difficulty, algo_num):
        recom_1.push(num, difficulty, algo_num)
        recom_2.push(num, difficulty, algo_num)
        recom_3.push(num, difficulty, algo_num)

m = int(si())
for _ in range(m):
    line = si().rstrip().split(" ")
    if line[0] == 'add':
        num, difficulty, algo_num = map(int, line[1:])
        if info.add(num, difficulty, algo_num):
            recom_1.push(num, difficulty, algo_num)
            recom_2.push(num, difficulty, algo_num)
            recom_3.push(num, difficulty, algo_num)
        
    elif line[0] == 'solved':
        info.solve(int(line[1]))

    elif line[0] == 'recommend':
        algo_num, searching_type = map(int, line[1:])
        print(recom_1.get_num_by_algo(algo_num, searching_type))

    elif line[0] == 'recommend2':
        searching_type = int(line[1])
        print(recom_2.get_num(searching_type))

    elif line[0] == 'recommend3':
        searching_type, l = map(int, line[1:])
        print(recom_3.get_num_from_diff(l, searching_type))
