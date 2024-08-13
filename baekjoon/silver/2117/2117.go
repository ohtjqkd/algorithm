package main

import (
	"fmt"
	"math"
)

func main() {
	var n int

	fmt.Scan(&n)
	convertN := int(math.Ceil(float64(n) / 2))
	ans := convertN * (convertN - 1)
	if n%2 == 1 {
		ans -= (convertN - 1)
	}
	fmt.Println(ans)
}

// 1 2 3 4 5 6 7 8 9 10
// 0 0 1 1 2 2 3 3 4 4
