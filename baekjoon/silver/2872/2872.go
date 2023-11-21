// input
// 4
// 1
// 3
// 4
// 2
// output
// 2

package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r  = bufio.NewReader(os.Stdin)
	w  = bufio.NewWriter(os.Stdout)
	in = bufio.NewScanner(os.Stdin)
)

func main() {
	defer w.Flush()

	var n, ans, nxt int

	n = nextInt()
	ans, nxt = 0, n
	l := make([]int, n)
	for i := 0; i < n; i++ {
		l[i] = nextInt()
	}
	for i := n - 1; i >= 0; i-- {
		if l[i] == nxt {
			nxt--
		} else {
			ans++
		}
	}
	fmt.Fprintln(w, ans)
}

func nextInt() int {
	in.Scan()
	r := 0
	for _, c := range in.Bytes() {
		r = r*10 + int(c-'0')
	}
	return r
}
