package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func main() {
	var l, n int
	var mn, mx int = 0, 1001

	defer writer.Flush()
	fmt.Fscan(reader, &l)
	s := make([]int, l)
	for i := 0; i < l; i++ {
		fmt.Fscan(reader, &s[i])
	}

	fmt.Fscan(reader, &n)
	for _, v := range s {
		if v == n {
			fmt.Fprintln(writer, 0)
			return
		}
		if v < n && v > mn {
			mn = v
		} else if v > n && v < mx {
			mx = v
		}
	}
	fmt.Fprintln(writer, (n-mn)*(mx-n)-1)
}
