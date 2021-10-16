def solution(line):
    answer = []
    loc = []
    min_x, max_x = float('inf'), -float('inf')
    min_y, max_y = float('inf'), -float('inf')
    for a1, b1, c1 in line:
        for a2, b2, c2 in line:
            try:
                x1, x2, y1, y2 = b1*c2-b2*c1, a1*b2-a2*b1, -(a1*(b1*c2-b2*c1)+c1*(a1*b2-a2*b1)), b1*(a1*b2-a2*b1)
                if x1 % x2 == 0 and y1 % y2 == 0:
                    x, y = x1/x2, y1/y2
                    loc.append([int(x), int(y)])
                    min_x, max_x = min(min_x, int(x)), max(max_x, int(x))
                    min_y, max_y = min(min_y, int(y)), max(max_y, int(y))
                # 아래 코드는 교점을 구하는 공식을 바탕으로 만들어졌지만, 아마 부동소수점(?) 문제로 틀리는 케이스가 나타났다.
                # x, y = (b1*c2-b2*c1)/(a1*b2-a2*b1), -((b1*c2-b2*c1)/(a1*b2-a2*b1))*(a1/b1)-(c1/b1)
                # if x-int(x) == 0 and y-int(y) == 0:
                #     loc.append([int(x), int(y)])
                #     min_x, max_x = min(min_x, int(x)), max(max_x, int(x))
                #     min_y, max_y = min(min_y, int(y)), max(max_y, int(y))
            except Exception as e:
                continue
    answer = [["." for _ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]
    loc = list(map(lambda x: [x[0]-min_x, abs(x[1]-max_y)], loc))
    for x, y in loc:
        answer[y][x] = "*"
    answer = list(map(lambda x: ''.join(x), answer))
    return answer

print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))