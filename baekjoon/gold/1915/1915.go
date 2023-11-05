package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r *bufio.Reader = bufio.NewReader(os.Stdin)
	w *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n, m int

	defer w.Flush()

	fmt.Fscanf(r, "%d %d\n", &n, &m)
	board := make([]string, n)
	dp := make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		dp[i] = make([]int, m+1)
	}
	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%s\n", &board[i])
	}

	ans := 0

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if board[i][j] == '1' {
				dp[i+1][j+1] = min(dp[i][j+1], min(dp[i+1][j], dp[i][j])) + 1
				ans = max(ans, dp[i+1][j+1])
			}
		}
	}
	fmt.Fprintln(w, ans*ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
