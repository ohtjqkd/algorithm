# input: 1 16 16, 1 1 1, 1 2 3, 15 28 19
# output: 16, 1, 5266, 7980

E, S, M = list(map(int, input().split(" ")))

for i in range(15*28*19):
    if (i % 15)+1 == E and (i % 28)+1 == S and (i % 19)+1 == M:
        print(i+1)
        break