from collections import defaultdict

n = int(input())

nums = list(map(int, input().split(" ")))
num_dict = dict()
check = dict()

for i, nu in enumerate(nums):
    if not num_dict.get(nu, False):
        num_dict[nu] = set()
    num_dict[nu].add(i)

for i in range(n - 1):
    for j in range(i + 1, n):
        s = nums[i] + nums[j]
        for idx in num_dict.get(s, []):
            if i == idx or j == idx:
                continue
            check[idx] = 1

print(sum(check.values()))