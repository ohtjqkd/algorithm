#include <iostream>
#include <iomanip>
#include <limits>
#include <cmath>

int main() {
  double x1, y1, x2, y2, x3, y3, xx1, xx2, xx3, yy1, yy2, yy3, vx1, vx2, vy1, vy2, r;
  double rn = std::numeric_limits<double>::max(), rx = 0.0f;

  scanf("%lf %lf %lf %lf %lf %lf", &x1, &y1, &x2, &y2, &x3, &y3);
  
  double dots[3][2] = {{x1, y1}, {x2, y2}, {x3, y3}};
  for (int i = 0; i < 3; i++) { 
    xx1 = dots[i][0], yy1 = dots[i][1];
    xx2 = dots[(i + 1) % 3][0], yy2 = dots[(i + 1) % 3][1];
    xx3 = dots[(i + 2) % 3][0], yy3 = dots[(i + 2) % 3][1];

    vx1 = xx2 - xx1, vy1 = yy2 - yy1;
    vx2 = xx3 - xx1, vy2 = yy3 - yy1;
    if ((vx1 == 0 && vx2 == 0) || (vx1 != 0 && vx2 != 0 && vy1 / vx1 == vy2 / vx2)) continue;
    r = std::sqrt(std::pow(vx1, 2) + std::pow(vy1, 2)) + std::sqrt(std::pow(vx2, 2) + std::pow(vy2, 2));
    rn = std::min(rn, r);
    rx = std::max(rx, r);
  }
  if (rx == 0) {
    printf("-1.0\n");
  } else {
    printf("%.16f\n", (rx - rn) * 2);
  }
}