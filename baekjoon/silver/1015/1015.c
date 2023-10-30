#include "stdio.h"
#include "stdlib.h"

typedef struct idx_info
{
  int q[50];
  int front;
  int last;
} idx_info;

int compare(const void *a, const void *b);

int main()
{
  int n, v, A[1001], B[1001], r[1001];
  idx_info q[1001] = {0};

  scanf("%d", &n);
  for (int i = 0; i < n; i++)
  {
    scanf("%d", &v);
    A[i] = v;
    B[i] = v;
  }
  qsort(B, n, sizeof(int), compare);

  for (int i = 0; i < n; i++)
  {
    q[B[i]].q[q[B[i]].last++] = i;
  }
  for (int i = 0; i < n; i++)
  {
    if (i == n - 1)
      printf("%d\n", q[A[i]].q[q[A[i]].front++]);
    else
      printf("%d ", q[A[i]].q[q[A[i]].front++]);
  }
  return 0;
}

int compare(const void *a, const void *b)
{
  return *(int *)a - *(int *)b;
}