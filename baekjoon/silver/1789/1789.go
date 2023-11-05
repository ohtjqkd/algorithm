package main

import "fmt"

func main() {
	var s int

	fmt.Scan(&s)
	ans := 0
	for i := 0; i*(i+1)/2 <= s; i++ {
		ans++
	}
	fmt.Println(ans - 1)
}
