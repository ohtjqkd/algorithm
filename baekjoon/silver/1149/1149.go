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
	var n int

	defer writer.Flush()
	fmt.Fscan(reader, &n)
	costs := make([][]int, n)
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		costs[i] = make([]int, 3)
		fmt.Fscan(reader, &costs[i][0], &costs[i][1], &costs[i][2])
		dp[i] = make([]int, 3)
	}
	dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]

	for i := 1; i < n; i++ {
		for j := 0; j < 3; j++ {
			dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + costs[i][j]
		}
	}
	fmt.Fprintln(writer, min(min(dp[n-1][0], dp[n-1][1]), dp[n-1][2]))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
