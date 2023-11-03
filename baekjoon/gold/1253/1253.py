# TODO
# refactoring

from collections import defaultdict
result = 0
cand = defaultdict(list)
n = int(input())
nums = list(map(int, input().split(" ")))
for idx, n in enumerate(nums):
    cand[n].append(idx)
cand_perm = []
li = sorted(list(cand.items()))
print(li)
for i in range(len(li)):
    if li[i][0] == 0:
        continue
    for j in range(i + 1, len(li)):
        if li[j][0] == 0:
            continue
        cand_perm.append((li[i][0], li[j][0]))
if cand.get(0):
    for k, value in li:
        if k == 0:
            continue
        if len(value) > 1:
            cand_perm.append((0, k))
if len(cand.get(0, [])) > 2:
    cand_perm.append((0, 0))
possible = set()
for a, b in cand_perm:
    possible.add(a + b)
for p in possible:
    result += len(cand.get(p, []))
print(result)
# n = int(input())

# nums = list(map(int, input().split(" ")))
# num_dict = dict()
# check = dict()

# for i, nu in enumerate(nums):
#     if not num_dict.get(nu, False):
#         num_dict[nu] = set()
#     num_dict[nu].add(i)

# for i in range(n - 1):
#     for j in range(i + 1, n):
#         s = nums[i] + nums[j]
#         for idx in num_dict.get(s, []):
#             if i == idx or j == idx:
#                 continue
#             check[idx] = 1

# print(sum(check.values()))