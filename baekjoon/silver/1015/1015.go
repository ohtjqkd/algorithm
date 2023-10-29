package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func main() {
	var n int
	var A, B []int
	var ret []string

	iMap := make(map[int][]string, 1000)
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var tmp int
		fmt.Scan(&tmp)
		A = append(A, tmp)
		B = append(B, tmp)
	}
	sort.Slice(B, func(i, j int) bool {
		return B[i] < B[j]
	})
	for i := 0; i < n; i++ {
		iMap[B[i]] = append(iMap[B[i]], strconv.Itoa(i))
	}
	for i := 0; i < n; i++ {
		ret = append(ret, iMap[A[i]][0])
		iMap[A[i]] = iMap[A[i]][1:]
	}
	fmt.Println(strings.Join(ret, " "))
}
