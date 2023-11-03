package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	var s []int
	fmt.Scan(&n)
	for i := n; i > 0; i /= 10 {
		s = append(s, i%10)
	}
	// s = mergeSort(s)
	sort.Slice(s, func(i, j int) bool {
		return s[i] > s[j]
	})
	for _, v := range s {
		fmt.Print(v)
	}
	fmt.Println()
}

func mergeSort(arr []int) []int {
	l := len(arr)
	ret := make([]int, l)
	if l == 1 {
		ret[0] = arr[0]
		return ret
	}
	mid := l / 2

	left := mergeSort(arr[:mid])
	right := mergeSort(arr[mid:])
	i, j := 0, 0
	for k := 0; k < l; k++ {
		switch {
		case i == len(left):
			ret[k] = right[j]
			j++
		case j == len(right):
			ret[k] = left[i]
			i++
		case left[i] < right[j]:
			ret[k] = right[j]
			j++
		case left[i] >= right[j]:
			ret[k] = left[i]
			i++
		}
	}
	return ret
}
