package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, t int
	fmt.Scan(&t)
	for i := 0; i < t; i++ {
		fmt.Scan(&a, &b)
		a %= 10
		if a == 0 {
			fmt.Println(10)
		} else if a == 1 || a == 5 || a == 6 {
			fmt.Println(a)
		} else if a == 4 || a == 9 {
			b %= 2
			if b == 0 {
				fmt.Println((a * a) % 10)
			} else {
				fmt.Println(a)
			}
		} else {
			b %= 4
			if b == 0 {
				fmt.Println((a * a * a * a) % 10)
			} else {
				fmt.Println(int(math.Pow(float64(a), float64(b))) % 10)
			}
		}
	}
}
