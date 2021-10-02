from collections import defaultdict
import heapq as hq
## 3 <= n <= 200, 1<= s, a, b <= n, s != a, a != b, b != s

n, s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [
    3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

# heap을 써야 효율성 테스트 패스


def getMinDist(start, nodes, n):
    distances = [float('inf') if i != start else 0 for i in range(n+1)]
    need_visit = [(0, start)]
    while need_visit:
        nowDistance, nowNode = hq.heappop(need_visit)
        nextNodes = nodes[nowNode]
        for next in nextNodes:
            nextNode, fare = next
            if nowDistance + fare < distances[nextNode]:
                distances[nextNode] = nowDistance + fare
                hq.heappush(need_visit, (distances[nextNode], nextNode))
    return distances


def solution(n, s, a, b, fares):
    answer = float('inf')
    nodes = defaultdict(list)
    for fare in fares:
        now, next, f = fare
        nodes[now].append((next, f))
        nodes[next].append((now, f))
    minFares = {}
    # print(nodes)
    for start in range(1, n+1):
        minFares[start] = getMinDist(start, nodes, n)
    for i in range(1, n+1):
        # print("start", i)
        startFare = minFares[s]
        midNodeFare = minFares[i]
        # print(startFare[i], midNodeFare[a], midNodeFare[b])
        # print(startFare, midNodeFare)
        answer = min(answer, startFare[i] + midNodeFare[a] + midNodeFare[b])
    return answer


print(solution(n, s, a, b, fares))
