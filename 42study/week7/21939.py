from bisect import bisect, bisect_right, insort
from collections import deque, defaultdict
import sys
input = sys.stdin.readline
write = sys.stdout.write
# test case가 부족해..
# 틀림

# class Node:
#     def __init__(self, diff, number):
#         self.diff = diff
#         self.number = number
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self, root):
#         self.root = root

#     def insert(self, diff, number):
#         self.current_node = self.root
#         while True:
#             if diff < self.current_node.diff:
#                 if self.current_node.left != None:
#                     self.current_node = self.current_node.left
#                 else:
#                     self.current_node.left = Node(diff, number)
#                     break
#             elif diff > self.current_node.diff:
#                 if self.current_node.right != None:
#                     self.current_node = self.current_node.right
#                 else:
#                     self.current_node.right = Node(diff, number)
#                     break
#             else:
#                 if number < self.current_node.number:                    
#                     if self.current_node.left != None:
#                         self.current_node = self.current_node.left
#                     else:
#                         self.current_node.left = Node(diff, number)
#                         break
#                 else:
#                     if self.current_node.right != None:
#                         self.current_node = self.current_node.right
#                     else:
#                         self.current_node.right = Node(diff, number)
#                         break
    
#     def search(self, diff):
#         self.current_node = self.root
#         while self.current_node:
#             if self.current_node.diff == diff:
#                 return True
#             elif self.current_node.diff > diff:
#                 self.current_node = self.current_node.left
#             else:
#                 self.current_node = self.current_node.right
#         return False
    
#     def delete(self, diff, number):
#             # 삭제할 노드가 있는지 검사하고 없으면 False리턴
#             # 검사를 한 후에는 삭제할 노드가 current_node, 삭제할 노드의 부모 노드가 parent가 된다.
#             is_search = False
#             self.current_node = self.root
#             self.parent = self.root
#             while self.current_node:
#                 if self.current_node.diff == diff:
#                     if self.current_node.number == number:
#                         is_search = True
#                         break
#                     elif number < self.current_node.number:
#                         self.current_node = self.current_node.left
#                     else:
#                         self.current_node = self.current_node.right
#                 elif diff < self.current_node.diff:
#                     self.parent = self.current_node
#                     self.current_node = self.current_node.left
#                 else:
#                     self.parent = self.current_node
#                     self.current_node = self.current_node.right
#             if is_search == False:
#                 return False
#             # 삭제할 노드가 자식 노드를 갖고 있지 않을 때
#             if self.current_node.left == None and self.current_node.right == None:
#                 if diff < self.parent.diff:
#                     self.parent.left = None
#                 else:
#                     self.parent.right = None
            
#             # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(왼쪽 자식 노드)
#             elif self.current_node.left != None and self.current_node.right == None:
#                 if diff < self.parent.diff:
#                     self.parent.left = self.current_node.left
#                 elif diff > self.parent.diff:
#                     self.parent.right = self.current_node.left
#                 else:
#                     if number < self.parent.number:
#                         self.parent.left = self.current_node.left
#                     else:
#                         self.parent.right = self.current_node.left
#             # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(오른쪽 자식 노드)
#             elif self.current_node.left == None and self.current_node.right != None:
#                 if diff < self.parent.diff:
#                     self.parent.left = self.current_node.right
#                 elif diff > self.parent.diff:
#                     self.parent.right = self.current_node.right                
#                 else:
#                     if number > self.parent.number:
#                         self.parent.left = self.current_node.right
#                     else:
#                         self.parent.right = self.current_node.right

#             # 삭제할 노드가 자식 노드를 두 개 가지고 있을 때
#             elif self.current_node.left != None and self.current_node.right != None:
#                 self.change_node = self.current_node.right
#                 self.change_node_parent = self.current_node.right
#                 while self.change_node.left != None:
#                     self.change_node_parent = self.change_node
#                     self.change_node = self.change_node.left
#                 if self.change_node.right != None:
#                     self.change_node_parent.left = self.change_node.right
#                 else:
#                     self.change_node_parent.left = None
                    
#                 if diff < self.parent.diff:
#                     self.parent.left = self.change_node
#                     self.change_node.right = self.current_node.right
#                     self.change_node.left = self.current_node.left
#                 elif diff > self.parent.diff:
#                     self.parent.right = self.change_node
#                     self.change_node.left = self.current_node.left
#                     self.change_node.right = self.current_node.right
#                 else:
#                     if number < self.parent.number:
#                         self.parent.left = self.change_node
#                         self.change_node.right = self.current_node.right
#                         self.change_node.left = self.current_node.left
#                     else:
#                         self.parent.right = self.change_node
#                         self.change_node.left = self.current_node.left
#                         self.change_node.right = self.current_node.right

#             return True

#     def find_min(self):
#         node = self.root
#         # print(node.diff, node.number)
#         while node.left:
#             node = node.left
#             # print(node.diff, node.number)
#         if node == self.root:
#             return node.right.number
#         return node.number
    
#     def find_max(self):
#         node = self.root
#         # print(node.left.diff, node.left.number)
#         while node.right:
#             node = node.right
#             # print(node.diff, node.number)
#         if node == self.root:
#             return node.left.number
#         return node.number
    
#     def print_all_node(self):
#         q = deque([self.root])
#         while q:
#             curr = q.popleft()
#             # print(f"diff: {curr.diff}, num: {curr.number}")
#             if curr.left:
#                 q.append(curr.left)
#             if curr.right:
#                 q.append(curr.right)

# def search(tree, diff, number):
#     curr = 0
#     while curr < len(tree):
#         if diff < tree[curr][0]:
#             curr = curr * 2 + 1
#         elif diff > tree[curr][0]:
#             curr = curr * 2 + 2
#         else:
#             if number[curr][1] == number:
#                 return curr
#             elif number < [curr][1]:
#                 curr = curr * 2 + 1
#             else:
#                 curr = curr * 2 + 2
    



N = int(input())

where_number = [0] * 100001
command = []
init_pair = []
total_pair = []
for i in range(N):
    num, dif = map(int, input().split(" "))
    init_pair.append([num, dif])
    total_pair.append([num, dif])

M = int(input())


for _ in range(M):
    line = input().rstrip().split(" ")
    com = line[0]
    command.append(line)
    if com == "add":
        total_pair.append([int(line[1]), int(line[2])])
total_pair.sort(key = lambda x: (x[1], x[0]))
median = total_pair[len(total_pair)//2]
init_pair.sort(key = lambda x: (abs(x[1] - median[1]), abs(x[0] - median[0])))
# bst = BST(Node(init_pair[0][1], 5))

bst = []
for num, dif in init_pair:
    insort(bst, (dif, num))
    where_number[num] = dif
is_changed = False
# MAX_PROB = bst.find_max()
# MIN_PROB = bst.find_min()
for line in command:
    com = line[0]
    if com == "add":
        num, dif = int(line[1]), int(line[2])
        insort(bst, (dif, num))
        # bst.insert(dif, num)
        where_number[num] = dif
        is_changed = True
    elif com == "solved":
        num = int(line[1])
        # print(f"target_number: {num}, target_diff: {where_number[num]}")
        # bst.delete(where_number[num], num)
        idx = bisect_right(bst, (where_number[num], num))
        
        del(bst[idx-1])
        where_number[num] = 0
        is_changed = True
    else:
        want = int(line[1])
        if want == -1:
            if is_changed:
                # MIN_PROB = bst.find_min()
                is_changed = False
            # print(MIN_PROB)
            print(bst[0][1])
        if want == 1:
            if is_changed:
                # MAX_PROB = bst.find_max()
                is_changed = False
            print(bst[-1][1])
        print(bst)
            # print(MAX_PROB)

# 난이도 안에 set(): number
# 번호를 받으면 그 번호로 난이도 몇에 있는지 접근이 가능해야할 듯

# class Binary:
#     def __init__(self, number, difficulty, parent = None, left = None, right = None):
#         self.left = left
#         self.right = right
#         self.parent = parent
#         self.number = number
#         self.difficulty = difficulty
    
#     def add(self, number, difficulty):
#         if self.difficulty > difficulty:
#             if self.left == None:
#                 self.left = Binary(number, difficulty, self)
#             else:
#                 self.left.add(number, difficulty, self)
#         elif self.difficulty < difficulty:
#             if self.right == None:
#                 self.right = Binary(number, difficulty, self)
#             else:
#                 self.right.add(number, difficulty, self)
#         else:
#             if self.number < number:
#                 binary = Binary(number, difficulty, left = self)
#                 if self.parent == None:
#                     self.parent = Binary(number, difficulty, None)
#                     self.parent.left = self
#                 elif self.parent.left == self:
#                     self.parent.left = Binary(number, difficulty, self.parent, left = self)
#                 else:
#                     self.parent.right = Binary(number, difficulty, self.parent, left = self)
#             elif self.number > number:
#                 binary = Binary(number, difficulty, right = self)
#             if self.parent == None:
#                 self.parent = binary
#                 binary.left = self
#             elif self.parent.left == self:
#                 self.parent.left = Binary(number, difficulty, self.parent, left = self)
#             else:
#                 self.parent.right = Binary(number, difficulty, self.parent, left = self)
#                 if self.parent == None:
#                     self.parent = Binary(number, difficulty, None)
#                     self.parent.right = self
#                 elif self.parent.left == self:
#                     self.parent.left =  Binary(number, difficulty, self.parent)
#                 self.parent.left = 


# import sys
# from collections import deque, defaultdict

# input = sys.stdin.readline
# write = sys.stdout.write
# N = int(input())
# difficulty = [set() for _ in range(101)]
# where_number = [0] * 100001
# minimum, maximum = 101, 0
# need_sort = [0] * 101
# sorting_list = [[] for _ in range(101)]
# now_dif = deque([])
# result = []
# for i in range(N):
#     num, dif = map(int, input().split(" "))
#     difficulty[dif].add(num)
#     where_number[num] = dif
#     minimum = min(minimum, dif)
#     maximum = max(maximum, dif)


# for i in range(101):
#     sorting_list[i] = sorted(list(difficulty[i]))
# M = int(input())
# for _ in range(M):
#     line = input().rstrip().split(" ")
#     com = line[0]
#     if com == "add":
#         num, dif = int(line[1]), int(line[2])
#         if dif > 100:
#             continue
#         minimum = min(minimum, dif)
#         maximum = max(maximum, dif)
#         difficulty[dif].add(num)
#         where_number[num] = dif
#         need_sort[dif] = 1
#     elif com == "solved":
#         num = int(line[1])
#         difficulty[where_number[num]].remove(num)
#         need_sort[where_number[num]] = 1
#         if where_number[num] == minimum and len(difficulty[minimum]) == 0:
#             for i in range(minimum, 101):
#                 if difficulty[i]:
#                     minimum = i
#                     break
#         if where_number[num] == maximum and len(difficulty[maximum]) == 0:
#             for i in range(maximum, 0, -1):
#                 if difficulty[i]:
#                     maximum = i
#                     break
#     else:
#         want = int(line[1])
#         if want == -1:
#             if need_sort[minimum]:
#                 sorting_list[minimum] = sorted(list(difficulty[minimum]))
#             result.append(sorting_list[minimum][0])
#         if want == 1:
#             if need_sort[maximum]:
#                 sorting_list[maximum] = sorted(list(difficulty[maximum]))
#             result.append(sorting_list[maximum][-1])
# for r in result:
#     print(r)
#             else:
#                 for i in range(1, 101):
#                     if L[i]:
#                         if need_sort[i]:
#                             L[i].sort()
#                             need_sort[i] = 0
#                         write(str(L[i][0]) + "\n")
#                         break
#         elif want == 1:
#             if L[maximum]:
#                 print(L[maximum][-1])
#             else:
#                 for i in range(100, 0, -1):
#                     if L[i]:
#                         if need_sort[i]:
#                             L[i].sort()
#                             need_sort[i] = 0
#                         write(str(L[i][-1]) + "\n")
#                         break
# added = False
# for _ in range(int(input())):
#     line = input().split(" ")
#     com = line[0]
#     if com == "add":
#         added = True
#         num, dif = int(line[1]), int(  line[2])
#     elif com == "solved":

#         if len(is_solved[int(line[1])]) != 0:
#             is_solved[int(line[1])].pop()
#     else:
#         want = int(line[1])
#         if want == -1:
#             while minimum_heap:
#                 dif, num = heapq.heappop(minimum_heap)
#                 # write(num, ":", is_solved[num])
#                 if dif in is_solved[num]:
#                     write(num)
#                     heapq.heappush(minimum_heap, (dif, num))
#                     break
#                 # write(minimum_heap)
#         elif want == 1:
#             while maximum_heap:
#                 dif, num = heapq.heappop(maximum_heap)
#                 # write(num, ":", is_solved[-num])
#                 if -dif in is_solved[-num]:
#                     write(-num)
#                     heapq.heappush(maximum_heap, (-dif, -num))
#                     break    
# maximum_heap = []
# minimum_heap = []
# is_solved = [set() for _ in range(100002)] 
# for i in range(N):
#     num, dif = map(int, input().split(" "))
#     heapq.heappush(minimum_heap, (dif, num))
#     heapq.heappush(maximum_heap, (-dif,-num))
#     is_solved[num].add(dif)
# for _ in range(int(input())):
#     line = input().split(" ")
#     com = line[0]
                    
    # write(is_solved)
    # write(minimum_heap)
    # write(maximum_heap)

            
# def find_idx(li, num):
#     start, end = 0, len(li)
#     while start < end:
#         mid = (start + end) // 2
#         if li[mid] == num:
#             return mid
#         if li[mid] < num:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return (start + end) // 2


# class Binary:
#     def __init__(self, number, difficulty, parent = None, left = None, right = None):
#         self.left = left
#         self.right = right
#         self.parent = parent
#         self.number = number
#         self.difficulty = difficulty
    
#     def add(self, number, difficulty):
#         if self.difficulty > difficulty:
#             if self.left == None:
#                 self.left = Binary(number, difficulty, self)
#             else:
#                 self.left.add(number, difficulty, self)
#         elif self.difficulty < difficulty:
#             if self.right == None:
#                 self.right = Binary(number, difficulty, self)
#             else:
#                 self.right.add(number, difficulty, self)
#         else:
#             if self.number < number:
#                 binary = Binary(number, difficulty, left = self)
#                 if self.parent == None:
#                     self.parent = Binary(number, difficulty, None)
#                     self.parent.left = self
#                 elif self.parent.left == self:
#                     self.parent.left = Binary(number, difficulty, self.parent, left = self)
#                 else:
#                     self.parent.right = Binary(number, difficulty, self.parent, left = self)
#             elif self.number > number:
#                 binary = Binary(number, difficulty, right = self)
#             if self.parent == None:
#                 self.parent = binary
#                 binary.left = self
#             elif self.parent.left == self:
#                 self.parent.left = Binary(number, difficulty, self.parent, left = self)
#             else:
#                 self.parent.right = Binary(number, difficulty, self.parent, left = self)
#                 if self.parent == None:
#                     self.parent = Binary(number, difficulty, None)
#                     self.parent.right = self
#                 elif self.parent.left == self:
#                     self.parent.left =  Binary(number, difficulty, self.parent)
#                 self.parent.left = 