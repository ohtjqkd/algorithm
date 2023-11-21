# 히스토그램 가장 큰 직사각형

# 해당 문제는 allganize 2차 코테에서 나옴

import sys

input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == "0":
        break
    ret = 0
    numbers = list(map(int, line.split(" ")))[1:]
    numbers = [-1] + numbers + [-1]
    stack = [0]
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[stack[-1]]:
            ret = max(ret, numbers[i])
        else:
            min_height = numbers[stack[-1]]
            while stack and numbers[stack[-1]] > numbers[i]:
                j = stack.pop()
                min_height = min(min_height, numbers[j])
                ret = max(ret, (i - j) * min_height)
        stack.append(i)
    print(ret)
