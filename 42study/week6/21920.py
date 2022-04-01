# 서로소 평균
# 서로소가 뭐였지?

N = int(input())
A = list(map(int, input().split(" ")))
X = int(input())
M = max(A)
ret = []
# div = [0 for _ in range(X + 1)]
so = [1] * (M + 1)
div = set()
for i in range(2, X + 1):
    if X % i == 0:
        # div[i] = 1
        div.add(i)

for d in div:
    for j in range(d, M + 1, d):
        so[j] = 0

for a in A:
    if so[a]:
        ret.append(a)
print(sum(ret) / len(ret))