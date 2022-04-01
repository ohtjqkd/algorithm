# 소수 최소 공배수
# 결국 소수만 구하면됨

N = int(input())
A = set(map(int, input().split(" ")))

M = max(A) + 100
prime = [1] * M
for i in range(2, M):
    if prime[i]:
        for j in range(i + i, M, i):
            prime[j] = 0
ret = 1
for a in A:
    # if prime[a] == 1:
    #     prime[a] = 0
    ret *= a
if ret == 1:
    ret = -1
print(ret)

# 중복된 값들이 들어오네 바보냐