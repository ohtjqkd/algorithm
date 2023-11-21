#include <stdio.h>
int main(void)
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        int n;
        scanf("%d", &n);
        int dp[11] = {1, 1, 1};

        for (int j = 0; j<n;j++) {
            if (j+1 < n) {
                dp[j+1] += dp[j];
            }
            if (j+2 < n) {
                dp[j+2] += dp[j];
            }
            if (j+3 < n) {
                dp[j+3] += dp[j];
            }
        }
        printf("%d\n", dp[n-1]);
    }
}