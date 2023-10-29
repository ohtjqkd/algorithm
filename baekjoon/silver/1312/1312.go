package main

import "fmt"

func main() {
	var a, b, n, k, ans int

	fmt.Scan(&a, &b, &n)
	k = a % b
	for i := 0; i < n; i++ {
		k *= 10
		ans = k / b
		k %= b
	}
	fmt.Println(ans)
}
