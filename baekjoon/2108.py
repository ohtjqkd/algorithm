import sys
input = sys.stdin.readline
n = int(input())
count = [0] * 8001
sums, mins, maxs, mode, m_cnt, mid, mid_cnt = 0, 4000, -4000, 0, 0, 0, 0
for _ in range(n):
    number = int(input())
    count[number+4000] += 1
    sums += number
most_count = max(count)
for i in range(len(count)):
    if count[i] == 0:
        continue
    # 중앙값을 구함
    if mid_cnt < n//2+1:
        mid_cnt += count[i]
        mid = i-4000
    # 최빈수를 구함 편의상 max함수를 사용함
    if m_cnt < 2:
        if count[i] == most_count:
            mode = i - 4000
            m_cnt += 1
    # 최소값을 구함 최초 1회 갱신 후 통과
    if i-4000 < mins:
        mins = i-4000
    # 최대값을 구함 가장 큰 i를 만날 때까지 갱신
    if i-4000 > maxs:
        maxs = i-4000
print(round(sums/n))
print(mid)
print(mode)
print(maxs-mins)
