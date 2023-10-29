// input
// 5
// 5 4 1 3 2
// output
// Nice

package main

import "fmt"

func main() {
	var n int

	fmt.Scan(&n)
	s := make([]int, n)
	stack := []int{}
	for i := n - 1; i >= 0; i-- {
		var x int
		fmt.Scan(&x)
		s[i] = x
	}

	curr := 1
	for len(s) > 0 || len(stack) > 0 {
		if len(stack) > 0 && stack[len(stack)-1] == curr {
			stack = stack[:len(stack)-1]
			curr++
		} else {
			if len(s) > 0 {
				p := s[len(s)-1]
				if p != curr {
					stack = append(stack, p)
				} else {
					curr++
				}
				s = s[:len(s)-1]
			} else {
				break
			}
		}
	}
	if len(stack) > 0 {
		fmt.Println("Sad")
	} else {
		fmt.Println("Nice")
	}
}
