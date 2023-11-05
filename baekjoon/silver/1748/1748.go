package main

import (
	"fmt"
	"strconv"
)

func main() {
	var nStr string
	var n int

	ans := 0
	fmt.Scan(&nStr)
	n, _ = strconv.Atoi(nStr)
	for i := 0; i < len(nStr); i++ {
		ans += (i+1)*(min(n, pow(10, i+1))-pow(10, i)) + 1
	}
	fmt.Println(ans)
}

func pow(base, top int) int {
	ret := 1
	for i := 0; i < top; i++ {
		ret *= base
	}
	return ret
}
