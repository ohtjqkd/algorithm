package main

import "fmt"

func main() {
	var a, b int

	fmt.Scan(&a, &b)
	ans := 1
	for {
		switch {
		case a == b:
			fmt.Println(ans)
			return
		case a > b:
			fmt.Println(-1)
			return
		case b%2 == 0:
			ans++
			b /= 2
		case b%10 == 1:
			ans++
			b /= 10
		default:
			fmt.Println(-1)
			return
		}
	}
}
