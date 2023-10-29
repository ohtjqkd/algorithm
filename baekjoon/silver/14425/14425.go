package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, m int

	reader := bufio.NewReader(os.Stdin)
	s := make(map[string]bool, 10000)
	ans := 0
	fmt.Fscan(reader, &n, &m)
	for i := 0; i < n; i++ {
		var str string
		fmt.Fscan(reader, &str)
		s[str] = true
	}
	for i := 0; i < m; i++ {
		var str string
		fmt.Fscan(reader, &str)
		if s[str] {
			ans++
		}
	}
	fmt.Println(ans)
}
