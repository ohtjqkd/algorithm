import sys
input = sys.stdin.readline
print = sys.stdout.write()
n = int(input())

count = [0] * 10000

for i in range(n):
    count[int(input())-1] += 1

for i in range(10001):
    if count[i] == 0:
        continue
    for j in range(count[i]):
        print(str(i+1))
