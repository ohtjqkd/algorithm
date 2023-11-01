package main

import "fmt"

const (
	P = 1_000_000_007
)

func main() {
	var n, k, denom uint64
	fmt.Scan(&n, &k)

	denom = (factorial(k) * factorial(n-k)) % P
	fmt.Println(factorial(n) * pow(denom, P-2) % P)
}

func factorial(n uint64) uint64 {
	var ret uint64 = 1
	for i := n; i > 1; i-- {
		ret = (ret * i) % P
	}
	return ret
}

func pow(base, exp uint64) uint64 {
	var ret uint64 = 1
	for i := exp; i > 0; i /= 2 {
		if i%2 == 1 {
			ret *= base
			ret %= P
		}
		base = (base * base) % P
	}
	return ret
}
