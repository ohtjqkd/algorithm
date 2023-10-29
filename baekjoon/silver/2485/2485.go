// why get TLE?
// append to slice is slow?
// so start and end value as variable

package main

import (
	"fmt"
)

func main() {
	var n int
	var start, end int
	var prevValue int
	var currValue int
	dist := make(map[int]int, 100_000)

	fmt.Scan(&n)
	fmt.Scan(&prevValue)
	start = prevValue
	for i := 1; i < n; i++ {
		fmt.Scan(&currValue)
		if i == n-1 {
			end = currValue
		}
		dist[currValue-prevValue] = 1
		prevValue = currValue
	}

	var d []int
	for v := range dist {
		d = append(d, v)
	}

	a := d[0]
	for i := 1; i < len(d); i++ {
		a = gcd(a, d[i])
	}

	fmt.Println((end-start)/a + 1 - n)
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}
