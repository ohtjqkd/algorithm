package main

import (
	"fmt"
	"sort"
)

func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func main() {
	var s string
	var rs string
	var ans string = ""

	fmt.Scan(&s)
	rs = Reverse(s)
	for i := 2; i > 0; i-- {
		var cand []string
		for j := i; j < len(rs); j++ {
			cand = append(cand, rs[j:])
		}
		sort.Slice(cand, func(a, b int) bool {
			return cand[a] < cand[b]
		})
		ans += cand[0]
		rs = rs[:len(rs)-len(cand[0])]
	}
	ans += rs
	fmt.Println(ans)
}
