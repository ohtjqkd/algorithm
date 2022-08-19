# input
# 3 2
# 1 2 1 2 1 2
# output
# 2

from collections import deque

N, K = map(int, input().split(" "))
conv = deque(map(int, input().split(" ")))
robot_loc = deque([])
broken = 0
ret = 0

def unload_robot(robot_loc):
    if robot_loc and robot_loc[-1] == N - 1:
        robot_loc.pop()
    return robot_loc

while broken < K:
    ret += 1
    # Step1. 로봇과 함께 벨트 회전
    conv.appendleft(conv.pop())
    for i in range(len(robot_loc)):
        robot_loc[i] += 1
    robot_loc = unload_robot(robot_loc)        
    # Step2. 가장 먼저 올라간 로봇부터 벨트가 회전하는 방향으로 이동
    # 이동하려는 칸에 로봇이 없고 내구도가 1이상 남아 있어야함
    for i in range(len(robot_loc)):
        if conv[robot_loc[-i - 1] + 1] > 0 and (i == 0 or robot_loc[-i -1] + 1 != robot_loc[-i]):
            robot_loc[-i - 1] += 1
            conv[robot_loc[-i-1]] -= 1
            if conv[robot_loc[-i-1]] == 0:
                broken += 1
    robot_loc = unload_robot(robot_loc)
    # Step3. 올리는 칸에 내구도가 1이상이면 로봇을 올림
    if conv[0] > 0:
        robot_loc.appendleft(0)
        conv[0] -= 1
        if conv[0] == 0:
            broken += 1
    robot_loc = unload_robot(robot_loc)

print(ret)