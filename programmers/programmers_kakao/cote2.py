from heapq import heappop, heappush, heapify

# strs, t = ["ab", "na", "n", "a", "bn"], "nabnabn"
# strs, t = ["ba","na","n","a"], "banana"
# strs, t = ["app","ap","p","l","e","ple","pp"], "apple"
strs, t = ["ba","an","nan","ban","n"], "banana"
strs, t = ["ba","an","nan","ban","n"], "b" * 20000
def solution(strs, t):
    answer = float('inf')
    dp = [set() for _ in range(len(t))]
    dp[1] = set(strs)
    for i in range(2, len(t)):
        for j in range(1, i//2+1):
            f, s = dp[j], dp[i-j]
            for str1 in f:
                for str2 in s:
                    if str1+str2 == t or str2+str1 == t:
                        return i
                    dp[i].add(str1+str2)
                    dp[i].add(str2+str1)
        print(dp[i])
    print(dp[-1])
    # strs.sort(key=lambda x: len(x))
    # print(strs)
    # stack = [(1, -len(piece), piece) for piece in strs]
    # heapify(stack)
    # while stack:
    #     cnt, _ ,joined =heappop(stack)
    #     print(joined)
    #     if len(joined) > len(t):
    #         continue
    #     if joined == t:
    #         return cnt
    #     for piece in strs:
    #         heappush(stack, (cnt+1, -len(joined+piece), joined+piece))
    return answer if answer != float('inf') else -1

print(solution(strs, t))