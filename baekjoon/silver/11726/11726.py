n = int(input())

result = [1, 2]

for i in range(2, n):
    result.append((result[i-1] + result[i-2])%10007)
print(result[n-1])

# input
# 2