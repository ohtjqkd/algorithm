package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var n, k int

	reader := bufio.NewReaderSize(os.Stdin, 1000000)
	fmt.Fscan(reader, &n, &k)

	arr := make([]int, 0, n)
	for i := 0; i < n; i++ {
		var a int
		fmt.Fscan(reader, &a)
		arr = append(arr, a)
	}
	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})
	fmt.Println(arr[k-1])
}
