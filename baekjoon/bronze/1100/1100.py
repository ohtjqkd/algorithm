ret = 0

board = [input() for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (i+j)%2==0 and board[i][j] == 'F':
            ret += 1
print(ret)

# input
# .F.F...F
# F...F.F.
# ...F.F.F
# F.F...F.
# .F...F..
# F...F.F.
# .F.F.F.F
# ..FF..F.