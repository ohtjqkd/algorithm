import sys
input = sys.stdin.readline
while True:
    x, y, z = map(int, input().split())
    if x+y+z == 0:
        break
    sides = [x, y, z]
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        print('right')
    else:
        print('wrong')
