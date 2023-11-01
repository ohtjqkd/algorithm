package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n, k int

	fmt.Scan(&n, &k)

	var arr []int
	var ret []string
	for i := 1; i <= n; i++ {
		arr = append(arr, i)
	}
	i := -1
	for len(arr) > 0 {
		i = (i + k) % len(arr)
		ret = append(ret, strconv.Itoa(arr[i]))
		arr = append(arr[:i], arr[i+1:]...)
		i--
	}
	fmt.Printf("<%s>\n", strings.Join(ret, ", "))
}
