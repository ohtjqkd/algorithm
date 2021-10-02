def get_primes(n):
    visited = [0] * (n+1)
    primes = []
    for i in range(2,n+1):
        if visited[i] == 0:
            primes.append(i)
            for j in range((n//i)+1):
                visited[j*i] = 1
    return primes

n = int(input())

primes = get_primes(n)
for p in primes:
    while n%p == 0:
        print(p)
        n //= p
