import math

m = int(input())
n = int(input())
numbers = dict()
total = 0
min_v = 0
for i in range(n, m-1, -1):
    if i == 1:
        continue
    jud = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            jud = False
            break
    if jud:
        total += i
        min_v = i


# 어디가 틀렸지 이코드..
# min_v = n+1
# for i in range(m, n+1):
#     if i == 1:
#         continue
#     numbers[i] = True

# for i in range(2, int(math.sqrt(n))):
#     for j in range(2, n//i+1):
#         if m <= i*j and i*j <= n:
#             numbers[i*j] = False
# for i in numbers.keys():
#     if numbers[i] == True:
#         total += i
#         if i < min_v:
#             min_v = i

if total == 0:
    print(-1)
else:
    print(total)
    print(min_v)
