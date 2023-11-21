n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = sum(a)
b.sort()
for i in range(len(b)):
  ans += b[i] * i
print(ans)