n = int(input())
# 무식하게 푼거
# i = 0
# count = 0
# while n > 0:
#     if n % 3 == 0:
#         count = i+n//3
#     i += 1
#     n -= 5
# if count == 0:
#     print(-1)
# else:
#     print(count)
if n % 5 == 0:
    print(n//5)
elif n % 5 == 1:
    print(n//5+1)
elif n % 5 == 2 and n >= 12:
    print(n//5+2)
elif n % 5 == 3:
    print(n//5+1)
elif n % 5 == 4 and n >= 9:
    print(n//5+2)
else:
    print(-1)
