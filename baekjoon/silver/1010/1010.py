# mCn을 구하는 문제
# mPn // (m-n)!

def comb(M, N):
    return permutation(M, N)//fact(N)


def permutation(M, N):
    if N == 1:
        return M
    return M * permutation(M-1, N-1)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(30))
for _ in range(int(input())):
    N, M = map(int, input().split(" "))
    print(comb(M, N))
