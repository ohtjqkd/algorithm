// input
// ababc
// output
// 12

package main

import "fmt"

func main() {
	var s string

	fmt.Scan(&s)
	m := make(map[string]bool, 1000000)
	answer := 0

	for i := 0; i < len(s); i++ {
		for j := i + 1; j <= len(s); j++ {
			substr := s[i:j]
			m[substr] = true
		}
	}
	for substr := range m {
		if m[substr] {
			answer++
		}
	}
	fmt.Println(answer)
}
