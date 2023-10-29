#include "stdio.h"
#include "stdlib.h"

int min(int a, int b);

int main()
{
  int N, M, g, k;
  int *s;

  scanf("%d", &N);
  s = (int *)malloc(sizeof(int) * (N + 1));

  for (int i = 0; i < N; i++)
  {
    scanf("%d", &s[i]);
  }
  scanf("%d", &M);

  for (int i = 0; i < M; i++)
  {
    scanf("%d %d", &g, &k);
    if (g == 1)
    {
      for (int j = k - 1; j < N; j += k)
      {
        s[j] ^= 1;
      }
    }
    else
    {
      s[k - 1] ^= 1;
      for (int j = 0; j < min(N + 1 - k, k); j++)
      {
        if (s[k - 1 - j] == s[k - 1 + j])
        {
          s[k - 1 - j] ^= 1;
          s[k - 1 + j] ^= 1;
        }
        else
        {
          break;
        }
      }
    }
  }
  for (int i = 0; i < N; i += 20)
  {
    for (int j = i; j < min(i + 20, N); j++)
    {
      if (j != min(i + 20, N) - 1)
      {
        printf("%d ", s[j]);
      }
      else
      {
        printf("%d\n", s[j]);
      }
    }
  }
  return 0;
}

int min(int a, int b)
{
  return a < b ? a : b;
}