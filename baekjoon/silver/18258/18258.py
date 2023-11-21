import sys
from queue import Queue
from collections import deque
input = sys.stdin.readline
N = int(input())
# print = sys.stdout.write


# queue 구현
# class MyQue:

#     def __init__(self):
#         self.front = None
#         self.back = None
#         self.size = 0
#         self.func = {
#             "push": self.push,
#             "pop": self.pop,
#             "front": self.getFront,
#             "back": self.getBack,
#             "empty": self.isEmpty,
#             "size": self.getSize
#         }

#     def push(self, x):
#         node = Node(x)

#         if self.size == 0:
#             self.front, self.back = node, node
#         else:
#             self.back.next = node
#             node.prev = self.back
#             self.back = node
#         self.size += 1

#     def pop(self, dummy):
#         if not self.front:
#             return -1
#         ret = self.front.value
#         self.front = self.front.next
#         self.size -= 1
#         return ret

#     def getFront(self, dummy):
#         if not self.size:
#             return -1
#         return self.front.value

#     def getBack(self, dummy):
#         if not self.size:
#             return -1
#         return self.back.value

#     def isEmpty(self, dummy):
#         if self.size == 0:
#             return 1
#         else:
#             return 0

#     def getSize(self, dummy):
#         return self.size


# class Node:
#     def __init__(self, x):
#         self.value = x
#         self.prev = None
#         self.next = None

#     def setNext(self, node):
#         self.next = node

#     def setPrev(self, node):
#         self.prev = node


# q = MyQue()

# while True:
#     tmp = input().strip()
#     if not tmp:
#         break
#     inp = tmp.split(" ")
#     com = inp[0]
#     value = "" if len(inp) == 1 else inp[1]
#     ret = q.func[com](value)
#     if ret != None:
#         print(str(ret))


# dequeue library
que = deque([])
func = {
    "push": lambda x: que.append(x),
    "pop": lambda: que.popleft(),
    "empty": lambda: 1 if len(que) == 0 else 0,
    "front": lambda: que[0],
    "back": lambda: que[-1],
    "size": lambda: len(que)
}

while True:
    tmp = input().strip()
    if not tmp:
        break
    inp = tmp.split(" ")
    cmd = inp[0]
    if cmd == "push":
        que.append(inp[1])
    elif cmd == "pop":
        print(que.popleft() if len(que) != 0 else -1)
    elif cmd == "empty":
        print(1 if len(que) == 0 else 0)
    elif cmd == "front":
        print(que[0] if len(que) != 0 else -1)
    elif cmd == "back":
        print(que[-1] if len(que) != 0 else -1)
    elif cmd == "size":
        print(len(que))

    # if cmd == "push":
    #     func[cmd](inp[1])
    #     continue
    # else:
    #     if cmd == "empty":
    #         print("empty", len(que))
    #     try:
    #         print(func[cmd]())
    #     except:
    #         print(-1)
