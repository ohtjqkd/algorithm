package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func main() {
	var x1, y1, x2, y2, x3, y3 float64
	var rn = math.Inf(+1)
	var rx = 0.0

	defer writer.Flush()
	fmt.Fscanf(reader, "%f %f %f %f %f %f\n", &x1, &y1, &x2, &y2, &x3, &y3)
	dots := [][]float64{{x1, y1}, {x2, y2}, {x3, y3}}

	for i := 0; i < 3; i++ {
		xx1, yy1 := dots[i][0], dots[i][1]
		xx2, yy2 := dots[(i+1)%3][0], dots[(i+1)%3][1]
		xx3, yy3 := dots[(i+2)%3][0], dots[(i+2)%3][1]
		vx1, vy1 := xx2-xx1, yy2-yy1
		vx2, vy2 := xx3-xx1, yy3-yy1
		if (vx1 == 0 && vx2 == 0) || (vx1 != 0 && vx2 != 0 && vy1/vx1 == vy2/vx2) {
			continue
		} else {
			r := math.Sqrt(math.Pow(vx1, 2)+math.Pow(vy1, 2)) + math.Sqrt(math.Pow(vx2, 2)+math.Pow(vy2, 2))
			rn = math.Min(rn, r)
			rx = math.Max(rx, r)
		}
	}
	if rx == 0 {
		fmt.Fprintln(writer, "-1.0")
	} else {
		ans := (rx - rn) * 2
		if ans == math.Floor(ans) {
			fmt.Fprintf(writer, "%g.0\n", ans)
		} else {
			fmt.Fprintf(writer, "%g\n", float64(ans))
		}
	}
}
