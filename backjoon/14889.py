n = int(input())

S = [list(map(int, input().split())) for _ in range(n)]


def cal(start, link):
    cap_start = 0
    cap_link = 0
    for i in range(n//2-1):
        for j in range(i+1, n//2):
            cap_start += S[start[i]][start[j]] + S[start[j]][start[i]]
            cap_link += S[link[i]][link[j]] + S[link[j]][link[i]]
    return abs(cap_start-cap_link)


def bfs(start, link, m):
    ret = 10000000000
    if m == n:
        return cal(start, link)
    if len(start) < n//2:
        ret = min(bfs(start+[m], link, m+1), ret)
    if len(link) < n//2:
        ret = min(bfs(start, link+[m], m+1), ret)
    return ret


print(bfs([], [], 0))
