#include <stdio.h>

int n, k, cnt;
int dfs(int s, int *arr);

int main()
{
    int arr[12] = {
        0,
    };
    int *curr_idx = arr;
    scanf("%d %d", &n, &k);
    dfs(0, &arr);
    if (*arr == 0)
        printf("-1\n");
    else
    {
        while (*(curr_idx + 1) != 0)
            printf("%d+", *(curr_idx++));
        printf("%d\n", *curr_idx);
    }
    return 0;
}

int dfs(int s, int *arr)
{
    if (s == n)
    {
        cnt++;
        if (cnt == k)
            return 1;
        return 0;
    }
    for (int i = 1; i < 4; i++)
    {
        if (s + i > n)
            continue;
        *arr = i;
        if (dfs(s + i, arr + 1))
            return 1;
        else
            *arr = 0;
    }
    return 0;
}