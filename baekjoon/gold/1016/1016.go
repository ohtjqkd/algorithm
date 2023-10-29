package main

import (
	"fmt"
	"math"
)

func main() {
	var n, m int

	fmt.Scan(&n, &m)
	r := initValue[int](make([]int, m-n+1), 1)

	for _, v := range primeSquare(m) {
		startNum := int(math.Ceil(float64(n)/float64(v))) * v
		for j := startNum; j <= m; j += v {
			r[j-n] = 0
		}
	}
	ans := 0
	for _, v := range r {
		if v == 1 {
			ans++
		}
	}
	fmt.Println(ans)
}

func primeSquare(max int) []int {
	var square []int
	prime := initValue[int](make([]int, int(math.Sqrt(float64(max)))+1), 1)
	prime[0], prime[1] = 0, 0
	for i := 2; i < len(prime); i++ {
		if prime[i] == 1 {
			square = append(square, i*i)
			for j := i + i; j < len(prime); j += i {
				prime[j] = 0
			}
		}
	}
	return square
}

func initValue[T any](t []T, v T) []T {
	for i := range t {
		t[i] = v
	}
	return t
}
