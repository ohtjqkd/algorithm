# input
# 4
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
# HHTTTHHTTTHTHHTHHTTHTTTHHHTHTTHTTHTTTHTH
# HTHTHHHTHHHTHTHHHHTTTHTTTTTHHTTTTHTHHHHT
# output
# 0 0 0 0 0 0 0 38
# 38 0 0 0 0 0 0 0
# 4 7 6 4 7 4 5 1
# 6 3 4 5 3 6 5 6

P = int(input())
li = ['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH']
for _ in range(P):
    cnt = {c:0 for c in li}
    string = input()
    for i in range(len(string)-2):
        cnt[string[i:i+3]] += 1
    print(' '.join(map(str, cnt.values())))