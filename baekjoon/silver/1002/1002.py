import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    large_r = max(r1, r2)
    small_r = min(r1, r2)
    # 두 원이 겹치는 경우
    if distance == 0 and r1 == r2:
        print(-1)
    # 내접하는 경우
    elif distance == r1 + r2 or distance == large_r - small_r:
        print(1)
    # 교점이 2개인 경우
    elif large_r - small_r < distance and distance < r1 + r2:
        print(2)
    # 만나지 않는 경우
    else:
        print(0)
