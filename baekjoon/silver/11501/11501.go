// input
// 3
// 3
// 10 7 6
// 3
// 3 5 9
// 5
// 1 1 3 1 2
// output
// 0
// 10
// 5
package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()

	var t, n, ans, mx int

	fmt.Fscan(r, &t)
	for i := 0; i < t; i++ {
		fmt.Fscan(r, &n)
		price := make([]int, n)
		ans, mx = 0, 0
		for j := n - 1; j >= 0; j-- {
			fmt.Fscan(r, &price[j])
		}
		for j := 0; j < n; j++ {
			if mx < price[j] {
				mx = price[j]
			} else {
				ans += mx - price[j]
			}
		}
		fmt.Fprintln(w, ans)
	}
}
