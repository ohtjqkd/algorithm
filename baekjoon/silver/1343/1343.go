package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string

	fmt.Scan(&s)

	var sp []string

	cc := 0
	for i := 1; i < len(s)+1; i++ {
		if i < len(s) && s[i] == s[cc] {
			continue
		}
		sp = append(sp, s[cc:i])
		cc = i
	}
	for i, v := range sp {
		if v[0] == 'X' {
			sp[i] = replacePoly(len(v))
			if sp[i] == "" {
				fmt.Println(-1)
				return
			}
		}
	}
	fmt.Println(strings.Join(sp, ""))
}

func replacePoly(n int) string {
	var ret []string

	if n%2 == 1 {
		return ""
	}
	for i := 0; i < n/4; i++ {
		ret = append(ret, "AAAA")
	}
	n %= 4
	for i := 0; i < n/2; i++ {
		ret = append(ret, "BB")
	}
	return strings.Join(ret, "")
}
