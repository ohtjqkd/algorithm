from collections import defaultdict

N = int(input())
A = list(map(int, input().split(" ")))

# 76% 실패 반례가 뭐가 있지
num_idx = defaultdict(dict)
for i, a in enumerate(A):
    num_idx[a][i] = True
dic = {}
answer = 0
print(num_idx)
for i in range(len(A)):
    for j in range(i+1, len(A)):
        s = A[i] + A[j]
        idxs = num_idx.get(s, False)
        if idxs and not dic.get(s):
            if not idxs.get(i, False) and not idxs.get(j, False):
                answer += 1
                dic[s] = True
                print(dic)
print(answer)


def func(target_idx):
    L, R = 0, N - 1
    target = a[target]