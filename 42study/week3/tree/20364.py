# 부동산 다툼

# 완전 2진 트리의 구조를 가지고 있음
# 땅의 개수 최대치가 2 ^ 20이기 때문에, 트리의 depth가 최대 20인 트리를 탐색하면 된다
# 최악의 경우 20 * 200000

import sys

input = sys.stdin.readline
N, Q = map(int, input().split(" "))

state = [0] * N # 땅이 점유됐는지 체크하는 list

for _ in range(Q):
    want = int(input()) # 목표땅
    # 탐색하는 과정에 점유된 땅이 없다면 0으로 출력하기 위해 ret = 0
    ret, now = 0, want 
    while now > 0:
        if state[now - 1] == 1: # 현재땅이 점유되어 있다면 결과값을 갱신해줌
            ret = now
        # now를 절반씩 줄여가면서 (부모땅의 인덱스) 탐색함
        now //= 2
    state[want - 1] = 1 # 탐색이 끝나면 맨처음 목표한 땅을 점유상태로 갱신
    print(ret)