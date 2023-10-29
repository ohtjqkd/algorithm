# 이분 매칭

# input
# 20
# 941 902 873 841 948 851 945 854 815 898 806 826 976 878 861 919 926 901 875 864
# output
# 806 926

# from collections import defaultdict

# prime = [True for _ in range(2_000 + 1)]
# prime[0], prime[1] = False, False
# for i in range(int(2_000 ** 0.5) + 1):
#   if prime[i]:
#     for j in range(i + i, len(prime), i):
#       prime[j] = False

# n = int(input())
# a = list(map(int, input().split()))
# t_s = defaultdict(set)

# even_set = set()
# odd_set = set()
# for i in range(len(a) - 1):
#   for j in range(i + 1, len(a)):
#     if prime[a[i] + a[j]]:
#       t_s[a[i]].add(j)
#       t_s[a[j]].add(i)
# for v in a:
#   if v == a[0]:
#     continue
#   if v % 2 == 0:
#     even_set.add(v)
#   else:
#     odd_set.add(v)
# def backtracking(v: int, e: set, o: set) -> bool:
#   print(e, o)
#   if len(e) != len(o):
#     return False
#   if len(e) == 0 and len(o) == 0:
#     return True
#   else:
#     for a in list(e):
#       e.remove(a)
#       for b in t_s.get(a, []):
#         if b in o:
#           o.remove(b)
#           if backtracking(v, e, o):
#             o.add(b)
#             e.add(a)
#             return True
#           o.add(b)
#       e.add(a)
#   return False
# ret = []
# for i in t_s.items():
#   print(i)
# for c in t_s.get(a[0]):
#   t = even_set if c % 2 == 0 else odd_set
#   for v in list(t):
#     t.remove(v)
#     if backtracking(c, even_set, odd_set):
#       ret.append(c)
#     t.add(v)
# print(ret)
  
  



import sys
import math

def dfs(x):
    global Y
    global matched
    global visited
    if visited[Y.index(x)]: return False
    visited[Y.index(x)] = True
    for y in Y:
        if primes[x + y]:
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

primes = [True for _ in range(2_000 + 1)]
primes[0], primes[1] = False, False
for i in range(int(2_000 ** 0.5) + 1):
  if primes[i]:
    for j in range(i + i, len(primes), i):
      primes[j] = False

answers = []
for i in X:
    matched = {}
    if i == X[0]: continue
    if primes[X[0] + i]:
        if N == 2:
            answers.append(i)
            break
        Y = [x for x in X[1:]]
        del Y[Y.index(i)]
        matched = {}
        for y in Y:
            visited = [False for _ in range(len(Y))]
            dfs(y)
    if N != 2 and len(matched) == N - 2: answers.append(i)
if not answers:
    answers.append(-1)
answers.sort()

print(' '.join(list(map(str, answers))))