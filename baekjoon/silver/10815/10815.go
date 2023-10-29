// input
// 5
// 6 3 2 10 -10
// 8
// 10 9 -5 2 3 4 5 -10
// output
// 1 0 0 1 1 0 0 1
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var n, m int

	belong := make(map[int]bool)

	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &m)
		belong[m] = true
	}
	fmt.Fscan(reader, &m)
	ret := make([]string, m)
	for i := 0; i < m; i++ {
		var value int
		fmt.Fscan(reader, &value)
		if belong[value] {
			ret[i] = "1"
		} else {
			ret[i] = "0"
		}
	}
	fmt.Println(strings.Join(ret, " "))
}
