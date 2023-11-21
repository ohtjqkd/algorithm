package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()

	var t, k int

	fmt.Fscan(r, &t)
	for i := 0; i < t; i++ {
		fmt.Fscan(r, &k)
		fmt.Fprintln(w, solve(k))
	}
}

func solve(k int) int {
	pages := make([]int, k)
	s := make([][]int, k)
	dp := make([][]int, k)
	for i := 0; i < k; i++ {
		fmt.Fscan(r, &pages[i])
		s[i] = make([]int, k)
		dp[i] = make([]int, k)
		for j := 0; j < k; j++ {
			if i == j {
				s[i][j] = pages[j]
				dp[i][j] = 0
			} else {
				s[i][j] = 0
				dp[i][j] = math.MaxInt64
			}
		}
	}
	for i := 0; i < k; i++ {
		for j := i; j < k; j++ {
			if i != j {
				s[i][j] = s[i][j-1] + s[j][j]
			}
		}
	}
	for i := 1; i < k; i++ {
		for j := 0; j < k-i; j++ {
			for k := 0; k < i; k++ {
				r := dp[j][j+k]
				c := dp[j+k+1][j+i]
				dp[j][i+j] = min(dp[j][i+j], r+c+s[j][i+j])
			}
		}
	}
	return dp[0][k-1]
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
