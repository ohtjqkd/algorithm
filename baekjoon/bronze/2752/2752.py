# input: 3 1 2
# output: 1 2 3

li = list(map(int, input().split(" ")))
print(' '.join(map(str, sorted(li))))