package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int

	fmt.Scan(&n)
	a := getArrFromInput(n)
	b := getArrFromInput(n)

	sort.Slice(a, func(i, j int) bool {
		return a[i] < a[j]
	})
	sort.Slice(b, func(i, j int) bool {
		return b[i] > b[j]
	})

	ans := 0
	for i := 0; i < n; i++ {
		ans += a[i] * b[i]
	}
	fmt.Println(ans)
}

func getArrFromInput(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		fmt.Scan(&arr[i])
	}
	return arr
}
