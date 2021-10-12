import sys

n = int(input())
input = sys.stdin.readline
diction = []
for _ in range(n):
    string = input().rstrip()
    diction.append(string)
diction = list(set(diction))
diction.sort()
diction.sort(key=lambda i: len(i))
for w in diction:
    print(w)
