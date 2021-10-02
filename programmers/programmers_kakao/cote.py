n, signs = 3, [[0,1,0],[0,0,1],[1,0,0]]

def solution(n,signs):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    nodes = dict()
    for i in range(len(signs)):
        for j in range(len(signs[0])):
            if signs[i][j] == 1:
                nodes[i] = nodes.get(i, []) + [j]
    print(nodes)
    for i in range(n):
        dfs(i, nodes, answer)
    return answer
    
def dfs(start, nodes, ret):
    stack = [start]
    while stack:
        print(ret)
        now = stack.pop()
        nxt = nodes.get(now)
        print(now, nxt)
        if not nxt:
            break
        else:
            for n in nxt:
                if ret[start][n] == 1:
                    break
                else:
                    print('record')
                    ret[start][n] = 1
                    stack.append(n)
    return ret    

solution(n, signs)