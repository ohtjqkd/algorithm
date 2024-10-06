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

	var N, M int
	fmt.Fscanf(reader, "%d %d\n", &N, &M)

	for i := 1; i <= N; i++ {
		pick(N, M-1, []int{i})
	}
}

func pick(n, m int, arr []int) {
	if m == 0 {
		for i := 0; i < len(arr); i++ {
			if i == len(arr)-1 {
				fmt.Fprintf(writer, "%d\n", arr[i])
			} else {
				fmt.Fprintf(writer, "%d ", arr[i])
			}
		}
	} else {
		for i := 1; i <= n; i++ {
			pick(n, m-1, append(arr, i))
		}
	}
}
