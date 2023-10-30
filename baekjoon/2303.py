# TODO
# Find another way

# input
# 3
# 7 5 5 4 9
# 1 1 1 1 1
# 2 3 3 2 10
# output
# 1
N = int(input())
max_value = 0
ret = 0
for i in range(N):
    cards = list(map(int, input().split(" ")))
    for j in range(len(cards)-2):
        for k in range(j+1, len(cards)-1):
            for l in range(k+1, len(cards)):
                S = (cards[j]+cards[k]+cards[l]) % 10
                if S >= max_value:
                    ret = i+1
                    max_value = S
print(ret)