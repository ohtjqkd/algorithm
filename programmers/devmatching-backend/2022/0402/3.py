# 사용되지 않는 간선을 제외한 간선 개수를 구하는 문제
# edges와 k, a, b가 주어짐
# a는 출발지점, b는 도착지점
# edges는 [p, q]이고 p와 q가 이어져있다는 의미
# k는 최대 가능 가중치이다. 만약 b까지 도착하는데 k보다 가중치의 합이 높을 경우 해당 경로는 고려하지 않음
# n <= 16
# k <= 8
# n - 1 <=  간선의 개수 <= min(50, n(n-1)/2) 이거였던거 같음
# back tracking으로 풀이함

def solution(edges, n, k, a, b):
    edge_dict = dict()
    for i in range(n):
        edge_dict[i] = []
    for p, q in edges:
        edge_dict[p].append(q)
        edge_dict[q].append(p)
    edge_table = [[0] * n for _ in range(n)]
    def back(curr, weight, used_edge):
        if weight > k:
            return
        elif weight <= k and curr == b:
            for p, q in used_edge:
                edge_table[p][q] = 1
        else:
            
