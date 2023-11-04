package main

import (
	"fmt"
	"math"
)

func main() {
	var b string

	fmt.Scan(&b)

	ans := 0
	for i := 0; i < len(b)-1; i++ {
		if b[i] != b[i+1] {
			ans++
		}
	}
	fmt.Println(int(math.Ceil(float64(ans) / 2)))
}
