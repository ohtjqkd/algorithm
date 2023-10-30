package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func main() {
	var T, N int
	var z1, o1, z2, o2 int
	defer writer.Flush()
	fmt.Fscanln(reader, &T)
	for i := 0; i < T; i++ {
		fmt.Fscanln(reader, &N)
		z1, o1, z2, o2 = 1, 0, 0, 1
		for j := 0; j < N-1; j++ {
			z1, o1, z2, o2 = z2, o2, z1+z2, o1+o2
		}
		if N == 0 {
			fmt.Fprintf(writer, "%d %d\n", z1, o1)
		} else {
			fmt.Fprintf(writer, "%d %d\n", z2, o2)
		}
	}
}
