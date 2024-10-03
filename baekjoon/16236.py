from collections import deque

class Shark:
    def __init__(self, size = 2, loc = [0, 0, 0]):
        self.size = size
        self.loc = loc
        self.eat_cnt = 0
        self.fish_cnt = 0

    def eat(self, size, r, c):
        if not self.can_eat(size):
            return False
        self.eat_cnt += 1
        self.fish_cnt -= 1
        self.loc = [r, c, 0]
        self.growup()
        return True
    
    def growup(self):
        if self.can_growup():
            self.size += 1
            self.eat_cnt = 0

    def can_eat(self, size):
        return self.size > size

    def can_growup(self):
        return self.eat_cnt >= self.size

def solution():
    N = int(input())
    M = [list(map(int, input().split(" "))) for _ in range(N)]
    shark = Shark(2, [0, 0])
    for r, row in enumerate(M):
        for c, col in enumerate(row):
            if col == 9:
                shark.loc = [r, c, 0]
            elif col != 0:
                shark.fish_cnt += 1
    dr, dc = [-1, 0, 0, 1], [0, -1, 1, 0]
    
    def recursive(ret):
        deq = deque([deque([shark.loc])])
        M[shark.loc[0]][shark.loc[1]] = 0
        visited = [[0 for _ in range(N)] for _ in range(N)]
        while deq and shark.fish_cnt > 0:
            depth = deq.popleft()
            nxt = deque([])
            cand = []
            while depth:
                r, c, w = depth.popleft()
                visited[r][c] = 1
                for i in range(4):
                    rr, cc = r + dr[i], c + dc[i]
                    if rr < 0 or N <= rr or cc < 0 or N <= cc or visited[rr][cc] == 1:
                        continue
                    if M[rr][cc] == 0 or M[rr][cc] == shark.size:
                        nxt.append([rr, cc, w + 1])
                    elif shark.can_eat(M[rr][cc]):
                        cand.append([rr, cc])
            if cand:
                cand.sort()
                rr, cc = cand[0]
                shark.eat(M[rr][cc], rr, cc)
                return recursive(ret + w + 1)
            if (nxt):
                deq.append(nxt)
        return ret
    return recursive(0)
print(solution())
