N = int(input())
string = input()
check = [0 for _ in range(26)]
start, end, answer = 0, 0, 0
alphas = set()
while end < len(string):
    alphas.add(string[end])
    check[ord(string[end]) - 97] += 1
    end += 1
    while len(alphas) > N:
        check[ord(string[start]) - 97] -= 1
        if check[ord(string[start]) - 97] == 0:
            alphas.remove(string[start])
        start += 1
    answer = max(answer, end - start)
    
print(answer)
    
