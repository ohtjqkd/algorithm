package main

import (
	"fmt"
	"math"
)

func main() {
	var n int

	ans := 0
	fmt.Scan(&n)
	for i := 1; i <= n; i++ {
		if hanNum(i) {
			ans++
		}
	}
	fmt.Println(ans)
}

func hanNum(n int) bool {
	exp := int(math.Log10(float64(n)))
	if exp == 0 {
		return true
	}
	arr := make([]int, exp+1)
	for i := 0; i <= exp; i++ {
		arr[exp-i] = n % 10
		n /= 10
	}
	diff := arr[0] - arr[1]
	for i := 1; i < exp; i++ {
		if arr[i]-arr[i+1] != diff {
			return false
		}
		diff = arr[i] - arr[i+1]
	}
	return true
}
