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

		dp := make([]int, n+1)
		for i := 0; i <= n; i++ {
			dp[i] = 1
		}

		for i := 2; i <= n; i++ {
			dp[i] += dp[i-2]
		}
		for i := 3; i <= n; i++ {
			dp[i] += dp[i-3]
		}

		fmt.Fprintln(writer, dp[n])
	}
}
