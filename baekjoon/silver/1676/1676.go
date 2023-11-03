package main

import "fmt"

func main() {
	var n int

	fmt.Scan(&n)
	t, f := 0, 0
	for i := 2; i < n+1; i++ {
		v := i
		for v%2 == 0 {
			v /= 2
			t++
		}
		for v%5 == 0 {
			v /= 5
			f++
		}
	}
	fmt.Println(min(t, f))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
