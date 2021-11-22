# input
# 5
# 1 5 3 2 4
# output
# 40

n = int(input())

location = list(map(int, input().split(" ")))
location.sort()
comb_n = [location[i]-location[i-1] for i in range(1, len(location))]
comb_cnt = len(comb_n)
part_cnt = [2 * (comb_cnt-i) * (i+1) for i in range(comb_cnt)]
print(sum([comb_n[i]*part_cnt[i] for i in range(comb_cnt)]))