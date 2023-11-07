package main

import "fmt"

func main() {
	var n int

	fmt.Scan(&n)
	ans := 0

	for i := n / 5; i > 0; i-- {
		m := n - i*5
		if m == 1 || m == 3 {
			continue
		}
		ans += i
		n = m
		break
	}
	if n%2 != 0 {
		fmt.Println(-1)
	} else {
		fmt.Println(ans + n/2)
	}
}
