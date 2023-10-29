package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func main() {
	var t int
	var s string

	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)
	writer := bufio.NewWriterSize(os.Stdout, 1024*1024)
	defer writer.Flush()
	fmt.Fscan(reader, &t)

	p := regexp.MustCompile(`^(100+1+|01)+$`)
	for i := 0; i < t; i++ {
		fmt.Fscan(reader, &s)
		if len(s) == len(p.FindString(s)) {
			fmt.Fprintln(writer, "YES")
		} else {
			fmt.Fprintln(writer, "NO")
		}
	}
}
