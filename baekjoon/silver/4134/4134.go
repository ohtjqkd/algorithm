package main

import "fmt"

func main() {
	var t int

	fmt.Scan(&t)
	for i := 0; i < t; i++ {
		var n int

		fmt.Scan(&n)
		for isPrime(n) == false {
			n++
		}
		fmt.Println(n)
	}
}

func isPrime(n int) bool {
	if n == 0 || n == 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
