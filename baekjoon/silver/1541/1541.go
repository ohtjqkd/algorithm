package main

import (
	"fmt"
	"strconv"
)

func main() {
	var s string
	var e []string
	fmt.Scan(&s)

	curr := 0

	for i := 1; i < len(s); i++ {
		if isOperand(s[i]) {
			e = append(e, s[curr:i])
			e = append(e, string(s[i]))
			curr = i + 1
		} else if i == len(s)-1 {
			e = append(e, s[curr:i+1])
		}
	}

	f := add
	ans := 0
	for i, v := range e {
		if v == "-" {
			f = sub
		} else if v == "+" {
			continue
		} else {
			a, _ := strconv.Atoi(e[i])
			ans = f(ans, a)
		}
	}
	fmt.Println(ans)
}

func isNum(c byte) bool {
	return c >= '0' && c <= '9'
}

func isOperand(c byte) bool {
	return c == '+' || c == '-'
}

func sub(a, b int) int {
	return a - b
}

func add(a, b int) int {
	return a + b
}
