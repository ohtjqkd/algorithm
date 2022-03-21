# heap 구현해서 해보기
from collections import deque
import sys

input = sys.stdin.readline


# 내가 구현한거 -> 쓰레기
# class MyHeap:
#     def __init__(self):
#         self.len = 0
#         self.que = []
    
#     def push(self, value: tuple):
#         self.que.append(value)
#         self.len += 1
#         n = self.len - 1
#         while n > 0:
#             if self.que[n][0] >= self.que[(n - 1)//2][0]:
#                 break
#             self.swap(n, (n-1)//2)
#             n = (n-1)//2
    
#     def pop(self):
#         if self.len <= 0:
#             return -1
#         self.swap(0, self.len - 1)    
#         self.len -= 1
#         ret = self.que.pop()
#         self.heapify(0)
#         return ret

#     def heapify(self, i):
#         sidx = i
#         lidx = i * 2 + 1
#         ridx = i * 2 + 2
#         if lidx < self.len and self.que[lidx][0] < self.que[sidx][0]:
#             sidx = lidx
#         if ridx < self.len and self.que[ridx][0] < self.que[sidx][0]:
#             sidx = ridx
#         if i == sidx:
#             return
#         self.swap(i, sidx)
#         self.heapify(sidx)
#     def swap(self, a, b):
#         self.que[a], self.que[b] = self.que[b], self.que[a]


class MyHeap:

    def __init__(self):
        self.data = [None]

    def push(self, item):
        self.data.append(item)
        i = len(self.data) - 1
        while i > 1:
            if self.data[i][0] < self.data[(i // 2)][0]:
                self.data[i], self.data[(i // 2)] = self.data[(i // 2)], self.data[i]
                i = i // 2
            else: break

    def pop(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop()
            print(data)
            self.minHeapify(1)
        else:
            data = None
        return data

    def minHeapify(self, i):
        left = 2 * i
        right = (2 * i) + 1
        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if left < len(self.data) and self.data[i][0] > self.data[left][0]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.          
            smallest = left
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right < len(self.data) and self.data[i][0] > self.data[right][0]:            
        # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right
        if smallest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.minHeapify(smallest)




N = int(input())
M = int(input())
edges = [[] for _ in range(N)]
for i in range(M):
    s, e, c = map(int, input().split(" "))
    edges[s-1].append((e-1, c))
start, end = map(int, input().split(" "))
min_cost = [float('inf')] * N
min_cost[start-1] = 0
heap = MyHeap()
heap.push((0, start - 1))
while len(heap.data) > 1:
    cost, city = heap.pop()
    if min_cost[city] < cost:
        continue
    for next_city, weight in edges[city]:
        if cost + weight < min_cost[next_city]:
            heap.push((cost + weight, next_city))
            min_cost[next_city] = cost + weight
print(min_cost[end-1])