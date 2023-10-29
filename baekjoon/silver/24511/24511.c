#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
  int data;
  struct Node *next;
  struct Node *prev;
} Node;

typedef struct Deque
{
  int count;
  Node *front;
  Node *rear;
  int size;
} Deque;

void init_Queue(Deque *q, int size)
{
  q->rear = q->front = NULL;
  q->count = 0;
  q->size = size;
}

int is_full(Deque *q)
{
  return (q->count == q->size);
}

int is_empty(Deque *q)
{
  return (q->count == 0);
}

int push_rear(Deque *q, int data)
{
  if (is_full(q))
  {
    return (0);
  }
  Node *newNode;
  newNode = (Node *)malloc(sizeof(Node));
  newNode->data = data;
  newNode->next = NULL;
  newNode->prev = NULL;
  if (is_empty(q))
  {
    q->front = newNode;
    q->rear = newNode;
  }
  else
  {
    q->rear->next = newNode;
    newNode->prev = q->rear;
    q->rear = newNode;
    q->rear->next = NULL;
  }
  q->count++;

  return (1);
}

int push_front(Deque *q, int data)

{

  if (is_full(q))

  {

    return (0);
  }

  Node *newNode;

  newNode = (Node *)malloc(sizeof(Node));

  newNode->data = data;

  newNode->next = NULL;

  newNode->prev = NULL;

  if (is_empty(q))

  {

    q->front = newNode;

    q->rear = newNode;
  }

  else

  {

    q->front->prev = newNode;

    newNode->next = q->front;

    q->front = newNode;

    q->front->prev = NULL;
  }

  q->count++;

  return (1);
}

int pop_front(Deque *q)
{
  Node *ptr;
  int return_data;

  if (is_empty(q))
  {
    return (-1);
  }
  else
  {
    ptr = q->front;
    return_data = ptr->data;
    q->front = q->front->next;
    q->count--;
  }
  free(ptr);
  if (q->count == 0)
  {
    q->front = NULL;
    q->rear = NULL;
  }

  return return_data;
}

int pop_rear(Deque *q)
{
  Node *ptr;
  int return_data;

  if (is_empty(q))
  {
    return (-1);
  }
  else
  {
    return_data = q->rear->data;
    ptr = q->rear;
    q->rear = q->rear->prev;
    q->count--;
  }
  if (q->count == 0)
  {
    q->front = NULL;
    q->rear = NULL;
  }
  free(ptr);

  return return_data;
}

int main(void)
{
  int n;
  int m;
  int temp;
  int *queuestack;

  Deque dq;
  scanf("%d", &n);
  init_Queue(&dq, 1000000);
  queuestack = (int *)malloc(sizeof(int) * n);
  for (int i = 0; i < n; i++)
  {
    scanf("%d", &queuestack[i]);
  }
  for (int i = 0; i < n; i++)
  {
    scanf("%d", &temp);
    if (!queuestack[i])
      push_front(&dq, temp);
  }
  scanf("%d", &m);
  for (int i = 0; i < m; i++)
  {
    scanf("%d", &temp);
    push_rear(&dq, temp); // 여기
  }
  for (int i = 0; i < m; i++)
  {
    printf("%d", pop_front(&dq));
    if (i != m - 1)
      printf(" ");
  }
  printf("\n");
}