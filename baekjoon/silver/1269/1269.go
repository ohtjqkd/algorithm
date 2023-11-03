package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReaderSize(os.Stdin, 1024*1024)
	writer *bufio.Writer = bufio.NewWriterSize(os.Stdout, 1024*1024)
)

func main() {
	var n, m int

	defer writer.Flush()
	fmt.Fscan(reader, &n, &m)

	a := make(map[int]bool, 1024)
	b := make(map[int]bool, 1024)

	for i := 0; i < n; i++ {
		var x int
		fmt.Fscan(reader, &x)
		a[x] = true
	}

	for i := 0; i < m; i++ {
		var x int
		fmt.Fscan(reader, &x)
		b[x] = true
	}

	for k := range b {
		if a[k] && b[k] {
			a[k] = false
			b[k] = false
		}
	}

	var cnt int

	for k := range a {
		if a[k] {
			cnt++
		}
	}

	for k := range b {
		if b[k] {
			cnt++
		}
	}

	fmt.Fprintln(writer, cnt)
}
