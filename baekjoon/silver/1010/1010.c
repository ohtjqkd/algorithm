#include <stdio.h>

int main()
{
  unsigned long long t, n, m, r, i, j;

  scanf("%llu", &t);
  for (i = 0; i < t; i++)
  {
    scanf("%llu %llu", &n, &m);
    r = 1;
    for (j = 0; j < n; j++)
    {
      r *= m - j;
      r /= j + 1;
    }
    printf("%llu\n", r);
  }
}