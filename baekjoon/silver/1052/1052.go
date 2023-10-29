package main

import (
	"fmt"
	"strings"
)

func main() {
	var n, k int

	fmt.Scanf("%d %d", &n, &k)
	ans := 0
	for strings.Count(fmt.Sprintf("%b", n), "1") > k {
		n++
		ans++
	}
	fmt.Println(ans)
}
