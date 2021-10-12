n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int, input().split())))
print(times)
times.sort(key=lambda x: abs(x[0]-x[1]))
print(times)
