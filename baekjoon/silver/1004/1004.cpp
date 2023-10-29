#include <iostream>
#include <cstring>
int powi(int x);

int main() {
  int t, n, x1, y1, x2, y2, cx, cy, r;
  std::cin >> t;

  for (int i = 0; i < t; i++) {
    int ans = 0;
    std::cin >> x1 >> y1 >> x2 >> y2;
    std::cin >> n;
    bool result[n];
    memset(result, false, sizeof(result));
    for (int j = 0; j < n; j++) {
      std::cin >> cx >> cy >> r;
      if (powi(x1 - cx) + powi(y1 - cy) < powi(r))
        result[j] = !result[j];
      if (powi(x2 - cx) + powi(y2 - cy) < powi(r))
        result[j] = !result[j];
    }
    for (int j = 0; j < n; j++) {
      if (result[j])
        ans++;
    }
    printf("%d\n", ans);
  }
  return 0;
}

int powi(int x) {
  return x * x;
}