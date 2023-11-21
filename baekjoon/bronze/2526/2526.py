# input: 67 31, 96 61
# output: 3, 60
N, P = map(int, input().split(" "))
div = P
idx = {N:0}
dp = [N]
while True:
    next_n = dp[-1]*N%P
    prev_idx = idx.get(dp[-1])
    if idx.get(next_n, False):
        start_idx = idx.get(next_n)
        break
    idx[next_n] = prev_idx+1
    dp.append(next_n)
print(len(dp)-start_idx)


