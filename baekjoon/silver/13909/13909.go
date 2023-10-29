package main

import (
	"fmt"
	"math"
)

func main() {
	var n int

	fmt.Scan(&n)
	fmt.Println(math.Floor(math.Sqrt(float64(n))))
}
