// input
// 3
// topcoder
// topcoder
// topcoding
// output
// 2

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()
	var n int
	var s string
	var l []string

	fmt.Fscanln(r, &n)
	ans := n
	for i := 0; i < n; i++ {
		fmt.Fscanln(r, &s)
		l = append(l, s)
	}
	sort.Slice(l, func(i, j int) bool {
		if len(l[i]) < len(l[j]) {
			return true
		} else if (len(l[i]) == len(l[j])) && (l[i] < l[j]) {
			return true
		}
		return false
	})

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if l[i] == l[j][:len(l[i])] {
				ans--
				break
			}
		}
	}
	fmt.Fprintln(w, ans)
}
