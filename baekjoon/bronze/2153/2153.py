# input: UFRN, contest
# output: It is a prime word. It is not a prime word.
map = dict(zip(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), range(1, 53)))
S = input()
n = 0
for s in S:
    n += map[s]
for i in range(2, n//2+1):
    if n%i == 0:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")