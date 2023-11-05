n, m = map(int, input().split())
def count_t(n):
    answer = 0
    i = 2
    while i <= n:
        answer += n//i
        i = i*2
    return answer

def count_f(n):
    answer = 0
    i = 5
    while i <= n:
        answer += n//i
        i = i*5
    return answer
two = 0
five = 0
two += count_t(n)
five += count_f(n)
two -= count_t(m)
five -= count_f(m)
two -= count_t(n-m)
five -= count_f(n-m)

print(min(two, five))
print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")