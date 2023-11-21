# input
# 2
# < >
# output
# 897
# 021


n = [i for i in range(10)]

def max_dfs(br, visited, prev):
    if len(br) == len(prev)-1:
        return prev
    for i in range(9, -1, -1):
        if visited[i] == 0 :
            if len(prev) == 0:
                visited[i] = 1
                prev.append(i)
            elif br[len(prev)-1] == "<" and prev[-1] < i:
                visited[i] = 1
                prev.append(i)
            elif br[len(prev)-1] == ">" and prev[-1] > i:
                visited[i] = 1
                prev.append(i)
            else:
                return None
            ret = max_dfs(br, visited, prev)
            if ret != None:
                return ret
            prev.pop()
            visited[i] = 0
def min_dfs(br, visited, prev):
    if len(br) == len(prev)-1:
        return prev
    for i in range(10):
        if visited[i] == 0 :
            if len(prev) == 0:
                visited[i] = 1
                prev.append(i)
            elif br[len(prev)-1] == "<" and prev[-1] < i:
                visited[i] = 1
                prev.append(i)
            elif br[len(prev)-1] == ">" and prev[-1] > i:
                visited[i] = 1
                prev.append(i)
            else:
                return None
            ret = min_dfs(br, visited, prev)
            if ret != None:
                return ret
            prev.pop()
            visited[i] = 0
    

k, br = int(input()), input().split(" ")
print(''.join(map(str, max_dfs(br, [0 for _ in range(10)], []))))
print(''.join(map(str, min_dfs(br, [0 for _ in range(10)], []))))