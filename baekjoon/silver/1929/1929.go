package main

import (
	"fmt"
	"math"
)

func main() {
	var m, n int

	fmt.Scan(&m, &n)

	prime := make([]int, n+1)
	prime[0], prime[1] = 1, 1
	for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
		for j := 2; j < n/i+1; j++ {
			prime[i*j] = 1
		}
	}
	for i, v := range prime {
		if v == 0 && m <= i && i <= n {
			fmt.Println(i)
		}
	}
}
