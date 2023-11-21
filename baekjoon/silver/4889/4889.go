// input
// }{
// {}{}{}
// {{{}
// ---     <--- eof signal
// output
// 1. 2
// 2. 0
// 3. 1
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

	var open, ans, cnt int
	var s string

	cnt = 1
	for {
		fmt.Fscanln(r, &s)
		if s[0] == '-' {
			break
		}
		open, ans = 0, 0
		for _, c := range s {
			if c == '{' {
				open++
			} else if c == '}' && open == 0 {
				ans++
				open++
			} else {
				open--
			}
		}
		fmt.Fprintf(w, "%d. %d\n", cnt, ans+open/2)
		cnt++
	}
}
