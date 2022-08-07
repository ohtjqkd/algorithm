N, K = map(int, input().split(" "))

par = 1
chil = 1
if K > N // 2:
    K = N - K
for i in range(N - K + 1, N + 1):
    par *= i
    par %= 1000000007
    print(par)
for j in range(1, K + 1):
    chil *= j
    chil %= 1000000007
    print(chil)
print(par // chil)
# print(ret % 1000000007)

# 538992043
# 