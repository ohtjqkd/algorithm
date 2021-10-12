# stack을 구현해보자
import sys
input = sys.stdin.readline


class Node():
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev
        self.next = None


class Stack():
    def __init__(self):
        self.root = Node('root')
        self.len = 0
        self.tail = self.root

    def push(self, value):
        push_node = Node(value)
        push_node.prev = self.tail
        self.tail.next = push_node
        self.tail = push_node
        self.len += 1

    def pop(self):
        if self.tail.value == 'root':
            return -1
        else:
            data = self.tail.value
            self.tail = self.tail.prev

            self.tail.next = None
            self.len -= 1
            return data

    def size(self):
        return self.len

    def empty(self):
        if self.len == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.tail.value == 'root':
            return -1
        else:
            return self.tail.value


stack = Stack()
for _ in range(int(input())):
    tmp = list(input().split())
    command = tmp[0]
    if command == 'push':
        stack.push(tmp[1])
    elif command == 'top':
        print(stack.top())
    elif command == 'size':
        print(stack.size())
    elif command == 'empty':
        print(stack.empty())
    elif command == 'pop':
        print(stack.pop())
