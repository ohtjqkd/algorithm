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

	var n, k int
	fmt.Fscanf(reader, "%d %d\n", &n, &k)

	var dp = make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, k+1)
	}

	var w, v int
	var weights, values []int
	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d %d\n", &w, &v)
		weights = append(weights, w)
		values = append(values, v)
	}

	for i := 1; i <= n; i++ {
		for j := 1; j <= k; j++ {
			if j < weights[i-1] {
				dp[i][j] = dp[i-1][j]
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]]+values[i-1])
			}
		}
	}

	fmt.Fprintf(writer, "%d\n", dp[n][k])
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
