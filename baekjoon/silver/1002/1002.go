package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	r *bufio.Reader = bufio.NewReader(os.Stdin)
	w *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var t int
	var x1, y1, r1, x2, y2, r2 float64
	var dist, l, s float64

	defer w.Flush()

	fmt.Fscanf(r, "%d\n", &t)

	for i := 0; i < t; i++ {
		fmt.Fscanf(r, "%f %f %f %f %f %f\n", &x1, &y1, &r1, &x2, &y2, &r2)
		dist = math.Sqrt(math.Pow(x1-x2, 2) + math.Pow(y1-y2, 2))
		l = max(r1, r2)
		s = min(r1, r2)
		if dist == 0 && r1 == r2 {
			fmt.Fprintln(w, -1)
		} else if dist == r1+r2 || dist == l-s {
			fmt.Fprintln(w, 1)
		} else if l-s < dist && dist < r1+r2 {
			fmt.Fprintln(w, 2)
		} else {
			fmt.Fprintln(w, 0)
		}
	}
}

func min(a, b float64) float64 {
	if a < b {
		return a
	}
	return b
}

func max(a, b float64) float64 {
	if a > b {
		return a
	}
	return b
}
