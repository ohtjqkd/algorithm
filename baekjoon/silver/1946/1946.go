// 참고한 코드
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

	var t, n int
	var a, b int
	var scores []int

	fmt.Fscanf(r, "%d\n", &t)
	for i := 0; i < t; i++ {
		ans := 0
		fmt.Fscanf(r, "%d\n", &n)
		scores = make([]int, n+1)
		for j := 0; j < n; j++ {
			fmt.Fscanf(r, "%d %d\n", &a, &b)
			scores[a] = b
		}
		last := scores[1]
		for k := 1; k < n+1; k++ {
			if last < scores[k] {
				ans++
			} else {
				last = scores[k]
			}
		}
		fmt.Fprintln(w, n-ans)
	}
}
