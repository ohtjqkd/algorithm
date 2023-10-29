#include "stdio.h"
#include "stdlib.h"

typedef struct hash_table
{

} t_hash_table;

typedef struct hash_map
{

} t_hash_map;

size_t hash_65599(const char *string, size_t len)
{
  size_t i;
  size_t hash;

  hash = 0;
  for (i = 0; i < len; ++i)
  {
    hash = 65599 * hash + string[i];
  }

  return hash ^ (hash >> 16);
}

typedef struct deque
{
  int q[1000];
  int front;
  int last;
} deque;

size_t hash_65599(int v, size_t len)
{
  size_t i;
  size_t hash;

  hash = 65599 * v;

  return hash ^ (hash >> 16);
}

void add()

    int compare(const void *a, const void *b);

int main()
{
  int n, v, A[1000], B[1000], r[1000];
  // values of line from second input, A, would be greater than 1000
  deque dq[1000];

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
    dq[B[i]].q[dq[B[i]].last++] = i;
  }

  for (int i = 0; i < n; i++)
  {
    deque *d = &dq[A[i]];
    r[i] = (*d).q[(*d).front++];
  }

  for (int i = 0; i < n; i++)
  {
    if (i == n - 1)
      printf("%d\n", r[i]);
    else
      printf("%d ", r[i]);
  }
  return 0;
}

int compare(const void *a, const void *b)
{
  return *(int *)a - *(int *)b;
}