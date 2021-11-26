# input: 0 4 2 5 6
# output: 1

print(sum(map(lambda x: x**2, list(map(int, input().split(" "))))) % 10)