package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader   *bufio.Reader = bufio.NewReader(os.Stdin)
	writer   *bufio.Writer = bufio.NewWriter(os.Stdout)
	sumValue int           = 0
)

func main() {
	defer writer.Flush()
	var n int

	fmt.Fscanf(reader, "%d\n", &n)
	hanoi(n, 1, 2, 3)
	fmt.Fprintf(writer, "%d\n", sumValue)
}

func hanoi(n, from, to, via int) {
	if n == 1 {
		fmt.Fprintf(writer, "%d %d\n", from, to)
		return
	}
	hanoi(n-1, from, via, to)
	fmt.Fprintf(writer, "%d %d\n", from, to)
	sumValue++
	hanoi(n-1, to, from, via)
}
