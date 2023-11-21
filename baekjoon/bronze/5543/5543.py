# sang = int(input())
# joong = int(input())
# ha = int(input())
# coke = int(input())
# cider = int(input())

# print(min(sang,joong, ha) + min(coke,cider) - 50)

# if 사용
min_burger = 2000
min_bev = 2000
for _ in range(3):
    v = int(input())
    if v < min_burger:
        min_burger = v
for _ in range(2):
    v = int(input())
    if v < min_bev:
        min_bev = v

print(min_burger+min_bev-50)
