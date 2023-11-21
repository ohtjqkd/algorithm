result = float('inf')
n = int(input())
for _ in range(n):
    n, t = map(int, input().split(" "))
    result = min(result, t // n)
print(result)