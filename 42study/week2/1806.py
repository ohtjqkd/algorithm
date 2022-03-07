N, S = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

curr_s = 0
start, end = 0, 0
answer = float('inf')
while end < len(A):
    curr_s += A[end]
    end += 1
    while start < end and curr_s >= S:
        if curr_s >= S:
            answer = min(answer, end - start)
        curr_s -= A[start]
        start += 1
if answer == float('inf'):
    print(0)
else:
    print(answer)
