#include <iostream>

const long long P = 1000000007;

long long factorial(long long n);
long long pow(long long base, long long exp);

int main() {
  long long n, k, denom;

  scanf("%lld %lld\n", &n, &k);
  denom = (factorial(k) * factorial(n - k)) % P;
  printf("%lld\n", (factorial(n) * pow(denom, P - 2)) % P);
}

long long factorial(long long n) {
    long long result = 1;
    for (long long i = 1; i <= n; i++) {
        result *= i;
        result %= P;
    }
    return result;
}

long long pow(long long base, long long exp) {
  long long ret = 1;
  for (long long i = exp; i > 0; i /= 2) {
    if (i % 2 == 1) {
      ret *= base;
      ret %= P;
    }
    base = (base * base) % P;
  }
  return ret;
}