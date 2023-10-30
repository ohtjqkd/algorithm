#include <iostream>

int min(int a, int b);

int main() {
  int n, l, k, ans;
  int easy, easy_cnt, hard, hard_cnt;
  
  easy_cnt = 0; hard_cnt = 0;
  scanf("%d %d %d\n", &n, &l, &k);
  for (int i = 0; i < n; i++) {
    scanf("%d %d\n", &easy, &hard);
    if (hard <= l) {
      hard_cnt++;
    } else if (easy <= l) {
      easy_cnt++;
    }
  }
  ans = min(hard_cnt, k) * 140;
  k -= min(hard_cnt, k);
  ans += min(easy_cnt, k) * 100;
  printf("%d\n", ans);

  return 0;
}

int min(int a, int b) {
  return a < b ? a : b;
}