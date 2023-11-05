package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n, v int
	var nbr, t, s []int
	var r []string

	defer writer.Flush()

	fmt.Fscanf(reader, "%d\n", &n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d\n", &v)
		t = append(t, v)
	}
	for i := n; i > 0; i-- {
		nbr = append(nbr, i)
	}

	idx := 0
	for len(nbr) > 0 || len(s) > 0 {
		if len(s) > 0 && t[idx] == s[len(s)-1] {
			s = s[:len(s)-1]
			r = append(r, "-")
			idx++
		} else if len(nbr) == 0 {
			r = append(r, "NO")
			r = r[len(r)-1:]
			break
		} else {
			s = append(s, nbr[len(nbr)-1])
			nbr = nbr[:len(nbr)-1]
			r = append(r, "+")
		}
	}
	for _, v := range r {
		fmt.Fprintln(writer, v)
	}
}
