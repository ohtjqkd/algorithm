from queue import PriorityQueue

# # priority que 구현

# class MyQue:

#     def __init__(self):
#         self.front = None
#         self.back = None
#         self.size = 0

#     def push(self, node):
#         try:
#             if self.size == 0:
#                 self.front, self.back = node, node
#                 self.back.prev = self.front
#                 self.size += 1
#                 return True
#             prev_node = self.back
#             while prev_node.value < node.value or prev_node.prev != None:
#                 print(prev_node.value)
#                 prev_node = prev_node.prev
#             prev_node.next, prev_node.next.prev = node, node
#             self.size += 1
#             return True
#         except Exception as e:
#             return False

#     def pop(self):
#         poped = [self.front.value, self.front.idx]
#         if self.size == 0:
#             return False
#         self.front = self.front.next
#         self.size -= 1
#         return poped


# class Node:

#     def __init__(self, value, idx):
#         self.value = value
#         self.idx = idx
#         self.prev = None
#         self.next = None


# C = int(input())
# for _ in range(C):
#     N, T = map(int, input().split(" "))
#     arr = list(map(int, input().split(" ")))
#     pq = MyQue()
#     result_idx = 0
#     for idx in range(N):
#         print(pq.push(Node(arr[idx], idx)))
#         print(pq.front.value)
#         print(pq.back.value)
#     while pq.size != 0:
#         value, popedIdx = pq.pop()
#         if popedIdx == T:
#             break
#         result_idx += 1

#     print("case end")


C = int(input())
for _ in range(C):
    N, T = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    que = PriorityQueue()
    for idx in range(N):
        value = arr[idx]
        que.put((-value, idx))
    cnt = 0
    print(que.queue)
    while que:
        value, idx = que.get()
        if idx == T:
            break
        cnt += 1
    print(cnt)
