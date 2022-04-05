# 연산 최대로

#몰라

N = int(input())
X = list(map(int, input().split(" ")))
P, Q = map(int, input().split(" "))







# 시간초과>!ㅒㅖㅑㅛㄲ ㅔㄹㄴㅎ요 펳노아ㅔㄹ허ㅣ # visited = [0] * (N + 1)
mem = [set() for _ in range(10)]
mem = set()
visited = [0] * (N + 1)
def gen_combinations(arr, visited, cnt, need):
    result = []
    if cnt == 0:
        target, rest = [], []
        for i in range(len(arr)):
            if visited[i] == need:
                target.append(arr[i])
            elif visited[i] == 0:
                rest.append(arr[i])
            if tuple(target) in mem:
                return []
            else:
                mem.add(tuple(target))
        return [[target, rest]]
    for i in range(1, len(visited)):
        if visited[i] != 0:
            continue
        visited[i] = need
        result.extend(gen_combinations(arr, visited, cnt - 1, need))
        visited[i] = 0
    return result

def dfs(arr, need, visited):
    ret = 0
    if not arr:
        return 0
    if need == 0:
        return sum(arr)
    for i in range(1, len(arr)):
        for now, rest in gen_combinations(arr, visited, i, need):
            ret = max(ret, sum(now) * dfs(rest, need - 1, visited))
    return ret

print(dfs(X, Q, visited))