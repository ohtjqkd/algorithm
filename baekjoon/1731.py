# input
# 4
# 364
# 843
# 1322
# 1801
# output
# 2280
# 3번째 수까지만 보면 등차인지 등비인지 알 수 있을껄?

N = int(input())
seq = [int(input()) for _ in range(N)]
same_diff  = (seq[1] - seq[0] == seq[2] - seq[1])
if same_diff:
    print(seq[-1] + seq[1] - seq[0])
else:
    print(seq[-1] * (seq[1] // seq[0]))