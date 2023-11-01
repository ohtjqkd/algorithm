package main

import "fmt"

func main() {
	var x int
	fmt.Scan(&x)

	s := fmt.Sprintf("%b\n", x)
	ans := 0
	for _, v := range s {
		if v == '1' {
			ans++
		}
	}
	fmt.Println(ans)
}
