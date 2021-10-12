n, k = map(int,input().split())
coins = []
answer = 0 
for _ in range(n):
    coins.append(int(input()))

for i in range(n-1,-1,-1):
    answer += (k//coins[i])
    k %= coins[i]
print(answer)