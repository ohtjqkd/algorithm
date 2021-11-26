# input
# 4 5 6 7 0 1 2 3 9 8
# 1 2 3 4 5 6 7 8 9 0
# output
# 16 13
# A

A, B = list(map(int, input().split(" "))), list(map(int, input().split(" ")))
a_cnt, b_cnt = 0, 0
last_winner = "D"
for i in range(len(A)):
    if A[i] > B[i]:
        a_cnt += 3
        last_winner = "A"
    elif A[i] < B[i]:
        b_cnt += 3
        last_winner = "B"
    else:
        a_cnt += 1
        b_cnt += 1
print(a_cnt, b_cnt)
if a_cnt == b_cnt:
    print(last_winner)
elif a_cnt > b_cnt:
    print("A")
else:
    print("B")