from collections import deque
def solution(rc, operations):
    row, col = len(rc), len(rc[0])
    deq_rc = deque([deque(r) for r in rc])
    def rotate(deq_rc):
        for i in range(row - 1):
            deq_rc[i].appendleft(deq_rc[i + 1].popleft())
            if i == 0:
                prev_pop = deq_rc[i].pop()
                continue
            tmp_pop = deq_rc[i].pop()
            deq_rc[i].append(prev_pop)
            prev_pop = tmp_pop
        deq_rc[-1].append(prev_pop)
        return deq_rc
    def shift_row(rc):
        rc.appendleft(rc.pop())
        return rc
    for o in operations:
        if o == "ShiftRow":
            deq_rc = shift_row(deq_rc)
        else:
            deq_rc = rotate(deq_rc)
    deq_rc = list(map(list, deq_rc))
    return deq_rc

tc = [
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],	["Rotate", "ShiftRow"],	[[8, 9, 6], [4, 1, 2], [7, 5, 3]]],
[[[8, 6, 3], [3, 3, 7], [8, 4, 9]],	["Rotate", "ShiftRow", "ShiftRow"],	[[8, 3, 3], [4, 9, 7], [3, 8, 6]]],
[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],	["ShiftRow", "Rotate", "ShiftRow", "Rotate"],	[[1, 6, 7 ,8], [5, 9, 10, 4]git, [2, 3, 12, 11]]]
]

for a,b,c in tc:
    print(solution(a, b))
