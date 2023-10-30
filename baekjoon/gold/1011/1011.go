package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var t, x, y, r, distance int

	defer writer.Flush()
	fmt.Fscanf(reader, "%d\n", &t)
	for i := 0; i < t; i++ {
		fmt.Fscanf(reader, "%d %d\n", &x, &y)
		distance = y - x
		if distance == 1 {
			fmt.Fprintln(writer, 1)
		} else if distance == 2 {
			fmt.Fprintln(writer, 2)
		} else {
			r = int(math.Sqrt(float64(distance)))
			if (r+1)*r < distance {
				r++
			}
			if distance <= r*r {
				fmt.Fprintln(writer, r*2-1)
			} else {
				fmt.Fprintln(writer, r*2)
			}
		}
	}
}
