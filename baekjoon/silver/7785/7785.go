// input
// 4
// Baha enter
// Askar enter
// Baha leave
// Artem enter
// output
// Askar
// Artem

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var n int
	var ans []string

	m := make(map[string]bool, 1000000)
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriterSize(os.Stdout, 10000000)
	defer writer.Flush()
	fmt.Fscan(reader, &n)

	for i := 0; i < n; i++ {
		var name, action string
		fmt.Fscan(reader, &name, &action)
		if action == "enter" {
			m[name] = true
		} else {
			m[name] = false
		}
	}

	for name := range m {
		if m[name] {
			ans = append(ans, name)
		}
	}
	sort.Slice(ans, func(i, j int) bool {
		return ans[i] > ans[j]
	})
	for _, name := range ans {
		fmt.Fprintln(writer, name)
	}
}
