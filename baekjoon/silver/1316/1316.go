package main

import "fmt"

func main() {
	var t int
	var s string

	fmt.Scan(&t)
	ans := 0
	for i := 0; i < t; i++ {
		fmt.Scan(&s)
		if check(s) {
			ans++
		}
	}
	fmt.Println(ans)
}

func check(s string) bool {
	var r []rune
	var visited [26]bool
	for i, c := range s {
		if i == 0 {
		} else if r[len(r)-1] == c {
			continue
		} else if visited[c-'a'] {
			return false
		}
		r = append(r, c)
		visited[c-'a'] = true
	}
	return true
}
