# input
# 10
# 40
# 30
# 60
# 30
# 20
# 60
# 30
# 40
# 50
# output
# 37
# 30
S = 0
max_freq_cnt, max_freq_num = 0, None
cnt = {}
for _ in range(10):
    n = int(input())
    S += n
    cnt[n] = cnt.get(n, 0) + 1
    if cnt[n] > max_freq_cnt:
        max_freq_cnt = cnt[n]
        max_freq_num = n

print(S//10)
print(max_freq_num)