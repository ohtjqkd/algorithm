package main

import (
	"fmt"
)

func main() {
	var n, m int
	var ans string
	fmt.Scan(&n)
	cost := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&cost[i])
	}
	fmt.Scan(&m)
	dp := make([]string, m+1)

	for i, v := range cost {
		if v > m {
			continue
		}
		dp[v] = fmt.Sprint(i)
	}
	for i := 0; i < m+1; i++ {
		for j := 0; j < n; j++ {
			if i+cost[j] > m || dp[i] == "" {
				continue
			}
			mx := maxString(dp[i], rune(j+'0'))
			if compare(mx, dp[i+cost[j]]) {
				dp[i+cost[j]] = mx
			}
		}
	}
	for _, v := range dp {
		if !compare(ans, v) {
			ans = v
		}
	}
	fmt.Println(ans)
}

func maxString(a string, b rune) string {
	for i, c := range a {
		if i == 0 && c == '0' {
			continue
		}
		if c <= b {
			return a[:i] + string(b) + a[i:]
		}
	}
	if a[0] == '0' {
		return "0"
	}
	return a + string(b)
}

func compare(a, b string) bool {
	if len(a) != len(b) {
		return len(a) > len(b)
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return a[i] > b[i]
		}
	}
	return false
}
