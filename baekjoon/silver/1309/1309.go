package main

import "fmt"

func main() {
	var n int

	fmt.Scan(&n)

	dp := make([]int, n+1)
	dp[0], dp[1] = 1, 3
	for i := 2; i <= n; i++ {
		dp[i] = (dp[i-1]*2 + dp[i-2]) % 9901
	}
	fmt.Println(dp[n])
}
