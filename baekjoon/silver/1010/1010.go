package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func main() {
	var t uint64
	var n, m, r, i, j uint64

	defer writer.Flush()
	fmt.Fscan(reader, &t)

	for i = 0; i < t; i++ {
		fmt.Fscan(reader, &n, &m)
		r = 1
		for j = 0; j < n; j++ {
			r *= (m - j)
			r /= (j + 1)
		}
		fmt.Fprintln(writer, r)
	}
}
