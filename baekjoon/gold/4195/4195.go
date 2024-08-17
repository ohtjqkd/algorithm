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
	defer writer.Flush()
	var tc int

	fmt.Fscanf(reader, "%d\n", &tc)
	for i := 0; i < tc; i++ {
		var n int
		fmt.Fscanf(reader, "%d\n", &n)

		parent := make(map[string]string)
		count := make(map[string]int)
		for j := 0; j < n; j++ {
			var a, b string
			fmt.Fscanf(reader, "%s %s\n", &a, &b)
			if _, ok := parent[a]; !ok {
				parent[a] = a
				count[a] = 1
			}

			if _, ok := parent[b]; !ok {
				parent[b] = b
				count[b] = 1
			}

			root1, root2 := find(a, parent), find(b, parent)

			if root1 == root2 {
				fmt.Fprintln(writer, count[root1])
			} else {
				count[root1] += count[root2]
				parent[root2] = root1
				fmt.Fprintln(writer, count[root1])
			}
		}
	}
}

func find(a string, parent map[string]string) string {
	if parent[a] == a {
		return a
	}

	parent[a] = find(parent[a], parent)
	return parent[a]
}
