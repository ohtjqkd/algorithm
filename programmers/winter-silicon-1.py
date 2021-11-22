from collections import defaultdict
def solution(rows, columns, connections, queries):
    answer = []
    edges = defaultdict(dict)
    for r1, c1, r2, c2 in connections:
        edges[(r1, c1)][(r2, c2)] = 1
        edges[(r2, c2)][(r1, c1)] = 1
    def get_side(rr1, cc1, rr2, cc2):

        side = []
        for i in range(rr1, rr2+1):
            for j in range(cc1, cc2+1):
                if i == rr1 or i == rr2 or j == cc1 or j == cc2:
                    side.append((i, j))
        return side
    for q in queries:
        rr1, cc1, rr2, cc2 = q
        if rr2 < rr1:
            rr1, rr2 = rr2, rr1
        if cc2 < cc1:
            cc1, cc2 = cc2, cc1
        sides = get_side(rr1, cc1, rr2, cc2)
        remove_cnt = 0
        for side in sides:
            con = edges.get(side, {})
            for k, v in con.items():
                if edges[side][k] == 1 and not ((rr1 <= k[0] <= rr2) and (cc1 <= k[1] <= cc2)):
                    print(k)
                    remove_cnt += 1
                    edges[side][k] = 0
                    edges[k][side] = 0
                print(edges)
        answer.append(remove_cnt)
    return answer

tc = [
    [4,3,[[1,1,2,1],[1,2,1,3],[1,3,2,3],[2,2,2,3],[2,2,3,2],[2,3,3,3],[3,2,3,3],[3,2,4,2],[4,1,4,2]],[[2,2,3,1],[1,2,4,2]],[4,2]],
    [2,2,[[1,1,1,2],[2,2,1,2],[2,1,1,1],[2,2,2,1]],[[1,1,2,2],[1,1,2,1],[2,1,2,2]],[0,2,2]],
    [3,3,[[1,1,2,1],[2,1,3,1],[1,2,2,2],[2,2,3,2],[1,3,2,3],[2,3,3,3]],[[1,1,3,1],[1,2,3,2],[1,3,3,3]],[0,0,0]]
]
for t in tc:
    print(f'expected {t[4]}')
    print(f'my answer {solution(t[0],t[1],t[2],t[3])}')
