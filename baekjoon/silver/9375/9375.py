from collections import defaultdict
for _ in range(int(input())):
    answer = 1
    graph = defaultdict(list)
    for _ in range(int(input())):
        name, part = input().split()
        graph[part].append(name)
    for i in graph.values():
        answer *= len(i)+1
    print(answer-1)
