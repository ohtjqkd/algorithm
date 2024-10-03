from collections import defaultdict

class Table:
    def __init__(self, n, m):
        self.table = [[Element(i, j, None) for j in range(n)] for i in range(m)]
        self.keyword = defaultdict(set)
    def merge(self, r1, c1, r2, c2):
        ele1, ele2 = self.table[r1][c1], self.table[r2][c2]
        if not ele1.value:
            ele1, ele2 = ele2, ele1
        self.keyword[ele1.value].discard(ele2)
        ele1.merge(ele2, self.table)
        
    def unmerge(self, r, c):
        self.table[r][c].unmerge(r, c, self.table)
        
    def update(self, r, c, value):
        ele = self.table[r][c]
        self.update_ele(ele, value)
        
    def update_ele(self, ele, value):
        self.keyword[ele.value].discard(ele)
        ele.value = value
        self.keyword[value].add(ele)
        
    def update_value(self, value1, value2):
        eles = self.keyword[value1]
        for e in list(eles):
            self.update_ele(e, value2)
    
    def get(self, r, c):
        return self.table[r][c]

    def print(self):
        for r in self.table:
            for c in r:
                print(c.value, end='')
            print()
        
class Element:
    def __init__(self, r, c, value):
        self.group = set()
        self.group.add((r, c))
        self.value = value
    
    def merge(self, src, table):
        for r, c in src.group:
            table[r][c] = self
        self.group.update(src.group)
    
    def unmerge(self, tr, tc, table):
        for r, c in self.group:
            if r == tr and c == tc:
                continue
            table[r][c] = Element(r, c, None)
            

def solution(commands):
    answer = []
    table = Table(50, 50)
    for cmd in commands:
        cmd = cmd.split(" ")
        if cmd[0] == "UPDATE":
            if cmd[1].isnumeric() and cmd[2].isnumeric():
                table.update(int(cmd[1]) - 1, int(cmd[2]) - 1, cmd[3])
            else:
                table.update_value(cmd[1], cmd[2])
        elif cmd[0] == "MERGE":
            r1, c1, r2, c2 = map(int, cmd[1:])
            table.merge(r1 - 1, c1 - 1, r2 - 1, c2 - 1)
        elif cmd[0] == "UNMERGE":
            r, c = map(int, cmd[1:])
            table.unmerge(r - 1, c - 1)
        elif cmd[0] == "PRINT":
            r, c = map(int, cmd[1:])
            ele = table.get(r - 1, c - 1)
            answer.append(ele.value if ele.value else "EMPTY")
    return answer

tc = [
    ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"],
    ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
]

for t in tc:
    print(solution(t))