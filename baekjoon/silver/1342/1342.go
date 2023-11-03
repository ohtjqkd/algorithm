package main

import "fmt"

var c map[rune]int = make(map[rune]int)

func main() {
	var s string
	fmt.Scan(&s)

	for _, v := range s {
		c[v]++
	}
	fmt.Println(dfs(0, len(s)))
}

func dfs(prev rune, n int) int {
	ret := 0
	if n == 0 {
		return 1
	}
	for k, _ := range c {
		if k != prev && c[k] > 0 {
			c[k]--
			ret += dfs(k, n-1)
			c[k]++
		}
	}
	return ret
}
