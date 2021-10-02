arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
arr = ["1", "-", "3", "+", "5", "-", "8"]
def solution(arr):
    answer = 1
    return dfs(arr)

def dfs(arr):
    answer = 0
    if len(arr) == 1:
        return arr[0]
    for i in range(1, len(arr), 2):
        if arr[i] == "-":
            answer = max(answer, dfs(arr[:i-1] + [int(arr[i-1])-int(arr[i+1])] + arr[i+2:]))
        else:
            answer = max(answer, dfs(arr[:i-1] + [int(arr[i-1])+int(arr[i+1])] + arr[i+2:]))
    return answer

print(solution(arr))