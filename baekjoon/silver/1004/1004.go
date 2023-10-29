package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func main() {
	var t, n, x1, y1, x2, y2, cx, cy, r int
	var result []bool

	defer writer.Flush()
	fmt.Fscan(reader, &t)
	for i := 0; i < t; i++ {
		var ans int = 0
		fmt.Fscan(reader, &x1, &y1, &x2, &y2)
		fmt.Fscan(reader, &n)
		result = make([]bool, n)
		for j := 0; j < n; j++ {
			fmt.Fscan(reader, &cx, &cy, &r)
			if powi(x1-cx)+powi(y1-cy) < powi(r) {
				result[j] = !result[j]
			}
			if powi(x2-cx)+powi(y2-cy) < powi(r) {
				result[j] = !result[j]
			}
		}
		for j := 0; j < n; j++ {
			if result[j] {
				ans++
			}
		}
		fmt.Fprintln(writer, ans)
	}
}

func powi(x int) int {
	return x * x
}
