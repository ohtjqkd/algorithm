// input
// 10
// 6 3 2 10 10 10 -10 -10 7 3
// 8
// 10 9 -5 2 3 4 5 -10
// output
// 3 0 0 1 2 0 0 2

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, m int
	var v int

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriterSize(os.Stdout, 10000000)
	defer writer.Flush()
	fmt.Fscan(reader, &n)
	s := make(map[int]int, 10000000)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &v)
		s[v]++
	}
	fmt.Fscan(reader, &m)
	for i := 0; i < m; i++ {
		fmt.Fscan(reader, &v)
		fmt.Fprint(writer, s[v])
		if i == m-1 {
			fmt.Fprint(writer, "\n")
			break
		}
		fmt.Fprint(writer, " ")
	}
}
