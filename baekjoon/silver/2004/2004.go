package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	fmt.Println(min(countT(n)-countT(m)-countT(n-m), countF(n)-countF(m)-countF(n-m)))
}

func countT(n int) int {
	ans := 0
	i := 2
	for i <= n {
		ans += n / i
		i *= 2
	}
	return ans
}

func countF(n int) int {
	ans := 0
	i := 5
	for i <= n {
		ans += n / i
		i *= 5
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
