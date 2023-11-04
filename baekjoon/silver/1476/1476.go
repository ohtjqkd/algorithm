package main

import "fmt"

func main() {
	var e, s, m int

	fmt.Scan(&e, &s, &m)
	for i := 0; i < 15*28*19; i++ {
		if i%15+1 == e && i%28+1 == s && i%19+1 == m {
			fmt.Println(i + 1)
			return
		}
	}
}
