package main

import "fmt"

func main() {
	var t int
	isPrime := [1000001]bool{}
	prime := make([]int, 100000)
	primeSet := make(map[int]bool, 100000)
	for i := 2; i < 1000001; i++ {
		isPrime[i] = true
	}
	for i := 2; i < 1000001; i++ {
		if isPrime[i] {
			prime = append(prime, i)
			primeSet[i] = true
			mul := 1
			for i*mul <= 1000000 {
				isPrime[i*mul] = false
				mul++
			}
		}
	}

	fmt.Scan(&t)
	for i := 0; i < t; i++ {
		var n, count int
		fmt.Scan(&n)
		for _, p := range prime {
			if primeSet[n-p] && p <= n-p {
				count++
			}
		}
		fmt.Println(count)
	}
}
