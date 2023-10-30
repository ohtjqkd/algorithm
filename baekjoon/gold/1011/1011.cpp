#include <iostream>
#include <math.h>
int main() {
  int t;
  float x, y, r, distance;

  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    scanf("%f %f", &x, &y);
    distance = y - x;
    if (distance == 1) {
      printf("1\n");
    } else if (distance == 2) {
      printf("2\n");
    } else {
      r = floor(sqrt(distance));
      if ((r + 1) * r < distance) {
        r += 1.0;
      }
      int r2 = static_cast<int>(r);
      if (distance <= r * r) {
        printf("%d\n", 2 * r2 - 1);
      } else {
        printf("%d\n", 2 * r2);
      }
    }
  }
}