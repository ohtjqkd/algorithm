package main

import (
	"fmt"
	"math"
)

func main() {
	var x int

	fmt.Scan(&x)

	dp := make([]int, x+1)
	dp[1] = 0
	for i := 2; i < x+1; i++ {
		dp[i] = math.MaxInt32
	}
	for i := 1; i < len(dp); i++ {
		if i+1 <= x {
			dp[i+1] = min(dp[i]+1, dp[i+1])
		}
		if i*3 <= x {
			dp[i*3] = min(dp[i]+1, dp[i*3])
		}
		if i*2 <= x {
			dp[i*2] = min(dp[i]+1, dp[i*2])
		}
	}
	fmt.Println(dp[x])
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
