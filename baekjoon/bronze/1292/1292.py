# input
# 3 7

a, b = list(map(int, input().split()))
arr = [j for j in range(1, 1001) for _ in range(1, j+1)]
print(sum(arr[a-1:b]))