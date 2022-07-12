def solution(n, m, x, y, queries):
    col_q, row_q = [], []
    for c, d in queries:
        div, mod = divmod(c, 2)
        if div == 0:
            if mod == 0:
                col_q.append(-d)
            else:
                col_q.append(d)
        else:
            if mod == 0:
                row_q.append(-d)
            else:
                row_q.append(d)

    def sub_f(axios_q: list, dest: int, wall: int):
        prev = dest
        ret = 1
        while axios_q:
            dd = axios_q.pop()
            # print('------------------')
            # print('prev', prev)
            # print('ret', ret)
            # print('dd', dd)
            # print('------------------')
            if dd < 0:
                ret += max(0, prev - dd - (wall - 1))
                prev = min(prev - dd, wall - 1)
            else:
                ret += max(0, - (prev - dd - 1))
                prev = min(prev - dd, wall - 1)
            # print(prev, ret)
        # print('------------------')
        # print('result', min(wall, ret))
        # print('------------------')
        return min(wall, ret)
            # for s in prev:
                # print(s, dd)
    #             if prev_min != 0 and 0 > dd:
    #                 prev_min = min(wall, prev_min - dd)
    #             if prev_max != wall - 1 and 0 < dd:
    #                 prev_max = max(0, prev_max - dd)
                
    #             if s == 0 and 0 > dd:

    #                 for i in range(min(wall, -dd + 1)):
    #                     # print('added', i)
    #                     nxt.add(i)
    #                 # print(nxt, wall)
    #             elif s == wall - 1 and dd > 0:
    #                 for i in range(max(0, wall - dd), wall):
    #                     # print('added', i)
    #                     nxt.add(i)
    #             if 0 <= s - dd < wall:
    #                 # print('added', s - dd)
    #                 nxt.add(s - dd)
    #             # print(nxt)
    #         prev = nxt
    #     # print('result', prev)
    #     return prev
    col = sub_f(col_q, y, m)
    # # print(col)
    row = sub_f(row_q, x, n)
    # print(row)
    
    # return True
    return col * row
    # return len(sub_f(col_q, y, m)) * len(sub_f(row_q, x, n))

n, m, x, y, queries = 2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]
n, m, x, y, queries = 2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]
n, m, x, y, query = 1000, 1000, 1, 1, [[0,100001],[2,100001]]

print(solution(n, m, x, y, queries))